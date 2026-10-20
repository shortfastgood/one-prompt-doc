"""Tests use model doubles and the real DocLang checker; no GPU is required."""

from contextlib import redirect_stderr, redirect_stdout
import io
import os
from pathlib import Path
import subprocess
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import Mock, patch

from PIL import Image

import mlx_vlm_doclang as cli


def document(body="<text>Alpha &amp; B</text>"):
    return f'<doclang xmlns="{cli.NS}" version="0.8">{body}</doclang>'


class PipelineTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.directory = Path(self.temp.name)
        self.image = self.directory / "source.png"
        Image.new("RGB", (100, 200), (21, 42, 63)).save(self.image)
        self.output = self.directory / "result.dclg"
        self.argv = ["--image", str(self.image), "--output", str(self.output)]
        self.calls = []

    def run_cli(self, outputs, extra=(), callback=None):
        results = iter(outputs)

        def model(image, instructions, task):
            self.calls.append((image.size, image.getpixel((0, 0)), instructions, task))
            if callback:
                callback()
            return next(results)

        self.stderr, stdout = io.StringIO(), io.StringIO()
        with patch.object(cli, "ModelRunner", return_value=model) as loader:
            with redirect_stderr(self.stderr), redirect_stdout(stdout):
                result = cli.main(self.argv + list(extra))
        self.assertEqual(stdout.getvalue(), "")
        self.loader = loader
        return result

    def test_defaults_and_exact_skill_directory(self):
        args = cli.parse_args(self.argv)
        self.assertEqual(args.model, "lmstudio-community/Qwen3.8-27B-MLX-4bit")
        self.assertEqual(args.max_token, 8192)
        self.assertEqual(str(cli.SKILL_DIR), "/Users/dden/gitroot/one-prompt-doc/.agents/skills/doclang")

    def test_image_references_prompt_review_and_output(self):
        first = document("<text>Alpha</text>")
        corrected = document("<text>Alpha and Beta</text>")
        self.assertEqual(self.run_cli([first, corrected], ["--model", "local/model", "--prompt", "Read all columns", "--max-token", "4096"]), 0)
        self.loader.assert_called_once_with("local/model", max_tokens=4096)
        self.assertEqual(self.output.read_text(), corrected)
        self.assertEqual(len(self.calls), 2)
        for size, pixel, instructions, _ in self.calls:
            self.assertEqual(size, (100, 200))
            self.assertEqual(pixel, (21, 42, 63))
            for name in ("SKILL.md", "references/syntax.md", "references/examples.md"):
                self.assertIn((cli.SKILL_DIR / name).read_text(), instructions)
        self.assertIn("Read all columns", self.calls[0][3])
        self.assertIn(first, self.calls[1][3])
        self.assertIn("Compare each source region", self.calls[1][3])
        self.assertIn("Checker exit 0", self.stderr.getvalue())
        self.assertEqual(list(self.directory.glob(".doclang-*")), [])

    def test_structural_errors_reach_review_and_final_repair(self):
        broken = document("<li>Wrong element</li>")
        self.assertEqual(self.run_cli([broken, broken, document()]), 0)
        self.assertEqual(len(self.calls), 3)
        self.assertIn("Unsupported element", self.calls[1][3])
        self.assertIn("Unsupported element", self.calls[2][3])

    def test_valid_flat_xml_still_gets_hierarchy_review(self):
        flat = document('<text>SECTION</text><text>Entry</text><text>Detail</text>')
        corrected = document(
            '<heading level="1">SECTION</heading><group>'
            '<heading level="2">Entry</heading><text>Detail</text></group>'
        )
        self.assertEqual(self.run_cli([flat, corrected]), 0)
        self.assertEqual(len(self.calls), 2)
        self.assertIn("Structural checks passed", self.calls[1][3])
        self.assertEqual(self.output.read_text(), corrected)

    def test_errors_after_final_repair_do_not_publish(self):
        self.assertEqual(self.run_cli(["<doclang>"] * 3), 1)
        self.assertEqual(len(self.calls), 3)
        self.assertFalse(self.output.exists())
        self.assertEqual(list(self.directory.glob(".doclang-*")), [])

    def test_requires_namespace_and_nonempty_document(self):
        for text in ('<doclang version="0.8"><text>A</text></doclang>', document("")):
            with self.subTest(text=text):
                self.assertEqual(self.run_cli([text] * 3), 1)
                self.assertFalse(self.output.exists())

    def test_unreadable_content_inspects_four_crops_once(self):
        unclear = document('<text><description>Unreadable content: serial number.</description></text>')
        broken = document("<li>Wrong</li>")
        self.assertEqual(self.run_cli([unclear] * 5 + [broken, unclear]), 0)
        self.assertEqual(len(self.calls), 7)
        self.assertEqual([call[0] for call in self.calls[1:5]], [(55, 110)] * 4)
        self.assertIn("(45, 90, 100, 200)", self.calls[5][3])
        self.assertIn("Avoid duplicates", self.calls[5][3])
        self.assertIn("Unreadable content remains", self.stderr.getvalue())

    def test_literal_marker_in_source_text_does_not_trigger_crops(self):
        text = document("<text>Unreadable content: is printed on the page.</text>")
        self.assertEqual(self.run_cli([text] * 2), 0)
        self.assertEqual(len(self.calls), 2)

    def test_output_extensions_preserve_xml_and_existing_files(self):
        for suffix in (".dclg", ".xml"):
            with self.subTest(suffix=suffix):
                output = self.output.with_suffix(suffix)
                extra = ["--output", str(output)]
                self.assertEqual(self.run_cli([document()] * 2, extra), 0)
                self.assertEqual(output.read_bytes(), document().encode("utf-8"))
                self.assertEqual(self.run_cli([], extra), 2)
                self.loader.assert_not_called()
                self.assertEqual(output.read_bytes(), document().encode("utf-8"))

    def test_missing_image_fails_before_model_load(self):
        self.image.unlink()
        self.assertEqual(self.run_cli([]), 2)
        self.loader.assert_not_called()

    def test_invalid_max_token_fails_before_model_load(self):
        for value in ("0", "-1", "1.5", "abc"):
            with self.subTest(value=value), patch.object(cli, "ModelRunner") as loader:
                with redirect_stderr(io.StringIO()), self.assertRaises(SystemExit) as error:
                    cli.main(self.argv + ["--max-token", value])
                self.assertEqual(error.exception.code, 2)
                loader.assert_not_called()
                self.assertFalse(self.output.exists())

    def test_missing_skill_fails_before_model_load(self):
        with patch.object(cli, "SKILL_DIR", self.directory):
            self.assertEqual(self.run_cli([]), 2)
        self.loader.assert_not_called()

    def test_bad_image_and_output_paths_fail_before_load(self):
        for extra in (["--output", str(self.directory / "x.txt")],
                      ["--output", str(self.directory / "no-extension")],
                      ["--output", str(self.directory / "missing" / "x.dclg")]):
            self.assertEqual(self.run_cli([], extra), 2)
            self.loader.assert_not_called()
        self.image.write_text("not an image")
        self.assertEqual(self.run_cli([]), 2)
        self.loader.assert_not_called()

    def test_existing_output_is_not_changed(self):
        self.output.write_text("original")
        self.assertEqual(self.run_cli([]), 2)
        self.loader.assert_not_called()
        self.assertEqual(self.output.read_text(), "original")

    def test_file_created_during_generation_is_not_changed(self):
        self.assertEqual(self.run_cli([document()] * 2, callback=lambda: self.output.write_text("other writer")), 1)
        self.assertEqual(self.output.read_text(), "other writer")

    def test_dangling_output_symlink_is_not_replaced(self):
        self.output.symlink_to(self.directory / "missing")
        self.assertEqual(self.run_cli([]), 2)
        self.assertTrue(self.output.is_symlink())
        self.loader.assert_not_called()

    def test_checker_process_failure_does_not_publish(self):
        failed = subprocess.CompletedProcess([], 2, "", "checker unavailable")
        with patch.object(cli.subprocess, "run", return_value=failed):
            self.assertEqual(self.run_cli([document()]), 1)
        self.assertFalse(self.output.exists())
        self.assertEqual(len(self.calls), 1)

    def test_absolute_skill_path_from_another_directory(self):
        old = Path.cwd()
        try:
            os.chdir(self.directory)
            self.assertEqual(self.run_cli([document()] * 2), 0)
        finally:
            os.chdir(old)


class ModelRunnerTests(unittest.TestCase):
    def setUp(self):
        # Exercise the real call adapter without importing MLX or allocating a GPU.
        self.runner = object.__new__(cli.ModelRunner)
        self.runner.config = {"model_type": "test"}
        self.runner.processor = object()
        self.runner.template_options = {}
        self.runner.context_limit = 32768
        self.runner.max_tokens = cli.DEFAULT_MAX_TOKENS
        self.runner.apply_template = Mock(return_value="formatted prompt")
        self.runner.add_special_tokens = Mock(return_value=False)
        self.ids = SimpleNamespace(shape=(1, 100))
        self.pixels = object()
        self.runner.prepare_inputs = Mock(return_value={"input_ids": self.ids, "pixel_values": self.pixels})
        self.runner.model = Mock()
        self.runner.model.get_input_embeddings.return_value = SimpleNamespace(inputs_embeds=SimpleNamespace(shape=(1, 829, 32)))
        self.result = SimpleNamespace(text=document(), generation_tokens=50, peak_memory=1.2, finish_reason="stop")
        self.runner.generate = Mock(return_value=self.result)
        self.image = Image.new("RGB", (10, 10))
        self.addCleanup(self.image.close)

    def call(self):
        with redirect_stderr(io.StringIO()):
            return self.runner(self.image, "skill instructions", "user task")

    def test_result_text_and_prepared_pixels(self):
        self.assertEqual(self.call(), document())
        _, kwargs = self.runner.generate.call_args
        self.assertIs(kwargs["pixel_values"], self.pixels)
        self.assertIs(kwargs["input_ids"], self.ids)
        self.assertIs(kwargs["image"][0], self.image)
        messages = self.runner.apply_template.call_args.args[2]
        self.assertEqual([m["role"] for m in messages], ["system", "user"])

    def test_processor_context_overflow_stops_before_embeddings(self):
        self.runner.context_limit = 8200
        with self.assertRaisesRegex(ValueError, "Context limit exceeded"):
            self.call()
        self.runner.model.get_input_embeddings.assert_not_called()
        self.runner.generate.assert_not_called()

    def test_expanded_image_tokens_are_counted(self):
        self.runner.context_limit = 8500  # Text fits, expanded vision sequence does not.
        with self.assertRaisesRegex(ValueError, "Context limit exceeded"):
            self.call()
        self.runner.generate.assert_not_called()

    def test_token_limit_rejects_even_closed_xml(self):
        self.result.finish_reason = "length"
        with self.assertRaisesRegex(ValueError, "output limit"):
            self.call()
        self.result.finish_reason = "stop"
        self.result.generation_tokens = self.runner.max_tokens
        with self.assertRaisesRegex(ValueError, "output limit"):
            self.call()

    def test_custom_max_token_controls_generation_and_output_limit(self):
        self.runner.max_tokens = 128
        self.assertEqual(self.call(), document())
        self.assertEqual(self.runner.generate.call_args.kwargs["max_tokens"], 128)
        self.result.generation_tokens = 128
        with self.assertRaisesRegex(ValueError, "output limit"):
            self.call()

    def test_custom_max_token_controls_context_allowance(self):
        self.runner.max_tokens = 128
        self.runner.context_limit = 829 + 128
        self.assertEqual(self.call(), document())
        self.runner.generate.reset_mock()
        self.runner.context_limit -= 1
        with self.assertRaisesRegex(ValueError, "829 input \\+ 128 output"):
            self.call()
        self.runner.generate.assert_not_called()

    def test_empty_model_response(self):
        self.result.text = "  "
        with self.assertRaisesRegex(ValueError, "no text"):
            self.call()

    def test_xml_wrappers_preserve_content(self):
        xml = document('<code><content>```python\nprint("A")\n```</content></code>')
        self.result.text = f"```xml\n{xml}\n```"
        self.assertEqual(self.call(), xml)
        self.result.text = f"Explanation\n```xml\n{xml}\n```"
        self.assertEqual(self.call(), xml)
        self.result.text = f"Explanation\n{xml}\nEnd of response."
        self.assertEqual(self.call(), xml)

    def test_normalization_does_not_select_between_documents_or_repair_xml(self):
        for text in (f"Intro\n{document()}\n{document()}",
                     f"Intro\n{document('<text>A & B</text>')}",
                     f"Intro\n{document()[:-len('</doclang>')]}"):
            with self.subTest(text=text):
                self.result.text = text
                self.assertEqual(self.call(), text)

    def test_text_only_processor_fails(self):
        self.runner.prepare_inputs.return_value = {"input_ids": self.ids}
        with self.assertRaisesRegex(ValueError, "image pixels"):
            self.call()
        self.runner.generate.assert_not_called()

    def test_system_role_fallback_is_limited(self):
        self.runner.apply_template.side_effect = [ValueError("System role not supported"), "prompt"]
        self.assertEqual(self.call(), document())
        self.assertIn("SKILL INSTRUCTIONS", self.runner.apply_template.call_args.args[2])
        self.runner.apply_template.side_effect = ValueError("Malformed image template")
        with self.assertRaisesRegex(ValueError, "Malformed"):
            self.call()


if __name__ == "__main__":
    unittest.main()
