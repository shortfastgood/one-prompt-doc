# DocLang extraction with MLX-VLM

The command reads a local PNG or JPEG image and writes a new UTF-8 DocLang XML file
with a `.dclg` or `.xml` extension.
It applies the skill at `/Users/dden/gitroot/one-prompt-doc/.agents/skills/doclang`.
The skill path is fixed, as specified in the implementation plan.

From the project root, use the existing environment:

```sh
development/mlx-vlm/.venv/bin/python development/mlx-vlm/mlx_vlm_doclang.py \
  --model lmstudio-community/Qwen3.8-27B-MLX-4bit \
  --prompt "Extract all text and preserve the document structure." \
  --max-token 8192 \
  --image ./data/bowers.jpg \
  --output ./output.dclg
```

`--model`, `--prompt`, and `--max-token` are optional. The model above is the default.
`--max-token` sets the maximum output tokens per model call. It defaults to `8192`
and must be a positive integer. For example, use `--max-token 16384` for a larger allowance.
The same limit applies to extraction, each crop inspection, review, and repair;
it is not a combined limit for the complete procedure.
`--image` and `--output` are required. The output directory must exist.
Both extensions use the same DocLang 0.8 format. For example, use `--output ./output.xml`.
The command does not overwrite an existing output file with either extension.
The model argument also accepts a local model directory.
Use a vision model supported by MLX-VLM with enough context for the skill,
image tokens, and the selected output allowance. Text-only MLX models cannot extract images.

For a new environment on an Apple Silicon Mac:

```sh
python3 -m venv .venv-doclang
.venv-doclang/bin/python -m pip install -r development/mlx-vlm/requirements-doclang.txt
.venv-doclang/bin/python development/mlx-vlm/mlx_vlm_doclang.py --help
```

Model IDs use the Hugging Face cache and can download model files.
Set `HF_HUB_OFFLINE=1` when all model files are already cached.
No LM Studio server or OpenAI API is needed.

## Skill execution

Python reads `SKILL.md`, `references/syntax.md`, and `references/examples.md`.
It sends those resources and the image pixels to the selected model.
It runs the skill's `scripts/check_doclang.py` with the current Python interpreter.
It then sends the draft, image, and checker messages to the model for review.

Extraction uses typography, alignment, spacing, and relationships between regions
to identify headings and logical groups. The instructions distinguish marginal
section headings from separate reading columns and request explicit heading levels.
Related headings, locations, dates or status, and content stay in the same group
when supported by the image. Bold text alone does not establish a heading.

The existing image review explicitly checks heading classification, levels,
group boundaries, and group membership, even when the XML checker passes.
It also distinguishes headings from captions, field labels, and emphasized body text.
The model must not invent structure.
The normal procedure uses two model calls: extraction and image review.

If the first draft marks unreadable content, Python inspects four overlapping crops.
The crop results stay associated with the same source page.
One further repair call is available if the reviewed XML fails structural checks.
The maximum is seven model calls, including four optional crop calls.

The model does not execute Python scripts or write the destination file.
Python performs those actions. It publishes a checked temporary file without replacing
an existing destination, including a file created by another process during generation.

Status messages go to standard error. Exit codes are `0` for completed output,
`2` for input errors, and `1` for model, checker, or output failures.
Each model call reserves the `--max-token` allowance and checks the model's context limit.
The input tokens plus this allowance must fit the context limit; the allowance is not reduced automatically.
A response that reaches the output limit is rejected, even if it contains an XML end tag.
One complete outer Markdown fence is removed without changing the XML inside it.
When the response includes commentary around a DocLang document, the program
parses the entire span from the first root start tag to the last root end tag.
It extracts that span only if it is one complete XML document with the required
namespace and version. It preserves the XML content, including nested code fences.
Malformed XML, incomplete XML, and responses with multiple DocLang documents remain subject
to the checker and bounded repair procedure. Normalization does not fix their contents.

## Automated verification

```sh
development/mlx-vlm/.venv/bin/python -m unittest discover \
  -s development/mlx-vlm -p 'test_mlx_vlm_doclang.py' -v

development/mlx-vlm/.venv/bin/python -m unittest discover \
  -s .agents/skills/doclang/scripts -p 'test_check_doclang.py' -v
```

The first suite uses model doubles and the actual checker. It needs no GPU.
It covers image pixels, skill resources, user prompts, review, repair limits,
crop offsets, token limits, XML checks, file-write races, and a different current directory.
It also checks the `--max-token` default, invalid values, custom generation limits,
and context boundaries with a custom allowance.
It checks that valid but flat XML still receives image review and that the
corrected heading hierarchy and groups are retained in the output.
The tests verify that readable drafts use two calls and that unreadable content triggers
the optional crops. They also check identical XML content and overwrite protection
for both `.dclg` and `.xml`, and rejection of unsupported or missing extensions.

## CV structure regression

Generate a new result for `data/CV-linear.png` with the default model:

```sh
development/mlx-vlm/.venv/bin/python development/mlx-vlm/mlx_vlm_doclang.py \
  --image data/CV-linear.png --output test/output/CV-linear.xml
```

Check that generated file without loading a model:

```sh
DOCLANG_CV_OUTPUT=test/output/CV-linear.xml \
  development/mlx-vlm/.venv/bin/python -m unittest discover \
  -s development/mlx-vlm -p 'test_cv_linear_structure.py' -v
```

The five checks verify eight headings with explicit levels, employment groups
with seven items each, the placement of `present`, the education group, and
the ten-item skills list in reading order. They expect 31 list items in total.
These expectations are specific to this image and are not part of the extraction program.
The tests are skipped unless `DOCLANG_CV_OUTPUT` is set.
They do not establish full transcription accuracy; compare wording with the image.
Use a new output path when repeating the command.

## Verification environment

Verification date: 19 October 2026.
The `--max-token` change was checked with automated tests on 20 October 2026.
The heading and grouping prompt change was checked on 20 October 2026.
The two-call workflow restoration and `.xml` support were checked with automated tests
on 20 October 2026. No additional model run was needed for these changes.
The model results below used the default allowance of 8192 tokens.

| Component | Version or value |
| --- | --- |
| Hardware | Apple M4 Max, 64 GiB unified memory |
| macOS | 26.6.2 |
| Python | 3.14.8 |
| mlx-vlm | 0.7.8 |
| mlx | 0.32.4 |
| Pillow | 12.3.0 |
| transformers | 5.19.0 |
| tokenizers | 0.23.3 |
| huggingface-hub | 2.2.0 |

## Model verification and limits

The synthetic document contains two text columns, a merged table header, form fields,
a selected checkbox, an obscured serial value, and a numbered list.
The photograph is the [MLX-VLM cats example](https://github.com/Blaizzy/mlx-vlm/blob/main/examples/images/cats.jpg).
Test inputs, logs, and generated files are in the ignored
`test/output/doclang-verification/` directory.

The bundled checker does not perform full XSD/Schematron validation or establish
transcription accuracy. A model can return structurally valid XML with invented or
missing content, even after its review call. Compare the output with the source image.
Model compatibility does not guarantee that the model can follow the full DocLang skill.

| Check | Result |
| --- | --- |
| CLI automated tests | 29 passed. |
| Bundled checker tests | 10 passed. |
| CV structure regression, default model (20 October) | All five checks passed on `CV-linear-enhanced.dclg`: eight headings at levels 1–3, seven nested groups, three employment lists of seven items, and ten skills items. The status and education associations passed. Two model calls. Peak MLX memory: 20.43 GB. |
| Default model, synthetic document (19 October, before the hierarchy prompt change) | Passed structural checks and source comparison. All reference text, reading order, three table rows, merged header, selected checkbox, and unreadable-value description matched. Six model calls. Peak MLX memory: 20.19 GB. |
| Default model, photograph (19 October, before the hierarchy prompt change) | Passed structural checks. Described two tabby cats, pink fabric, and two remote controls, with no invented transcription. The descriptions of the right cat's pose and its distance from a remote are approximate. Two model calls. Peak MLX memory: 19.85 GB. |

Model verification is limited to the default model, as requested.

For the CV, the supplied Python output had one heading, no groups, and 31 list items.
The enhanced output retains all 31 items and adds the tested hierarchy.
It also reads the first employer as `MACGYVER-GERHOLD`, which matches the image.
One known transcription error remains: the image says `writers? work`, but the output
says `writers' work`. Passing the hierarchy checks does not establish exact OCR accuracy.
The saved CV output is `test/output/CV-linear-enhanced.dclg` and its log is
`test/output/CV-linear-enhanced.log`. The supplied comparison files were not changed.

The always-on crop experiment was removed: it produced identical CV XML while
increasing the observed runtime from approximately 3.3 to 14.2 minutes.
The original crop fallback for unreadable content remains.

Default model revision: `6067b15cf581666a4aecf6af3afaba4bb5efc20c`.
The default document log is `test/output/doclang-verification/qwen-document-final.log`.
The corresponding output is `test/output/doclang-verification/qwen-document-final.dclg`.
The photograph log and output are `test/output/doclang-verification/qwen-photo-final.log`
and `test/output/doclang-verification/qwen-photo-final.dclg`.
