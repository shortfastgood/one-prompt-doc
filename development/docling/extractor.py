# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "docling-core",
#     "mlx-vlm",
#     "pillow",
#     "transformers",
# ]
# ///

import argparse
import webbrowser
from pathlib import Path

from docling_core.types.doc import ImageRefMode
from docling_core.types.doc.document import DocTagsDocument, DoclingDocument
from mlx_vlm import load, stream_generate
from mlx_vlm.prompt_utils import apply_chat_template
from mlx_vlm.utils import load_config
from transformers.image_utils import load_image

DEFAULT_MODEL = "ibm-granite/granite-docling-258M-mlx"
DEFAULT_PROMPT = "Convert this page to docling."
DEFAULT_MAX_TOKENS = 8192


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Examine an image and read the text with Docling (mlx)."
    )
    parser.add_argument("--model", default=DEFAULT_MODEL, help="The AI model to use.")
    parser.add_argument("--image", required=True, help="The path to the image.")
    parser.add_argument(
        "--max-tokens", type=int, default=DEFAULT_MAX_TOKENS, help="The limit for the number of tokens."
    )
    parser.add_argument("--prompt", default=DEFAULT_PROMPT, help="The prompt for the AI.")
    parser.add_argument("--output", required=True, help="The path to the output file.")
    parser.add_argument(
        "--showInBrowser",
        action="store_true",
        help="Show the result in the browser when the output format is HTML.",
    )
    parser.add_argument(
        "--trace",
        action="store_true",
        help="Write the doc-tags to the standard output.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    print("Loading model...")
    model, processor = load(args.model)
    config = load_config(args.model)

    print("Preparing input...")
    pil_image = load_image(args.image)
    formatted_prompt = apply_chat_template(processor, config, args.prompt, num_images=1)

    print("Generating DocTags...\n")
    output = ""
    for token in stream_generate(
        model, processor, formatted_prompt, [pil_image], max_tokens=args.max_tokens, verbose=False
    ):
        output += token.text
        if args.trace:
            print(token.text, end="")
        if "</doctag>" in token.text:
            break

    if args.trace:
        print()

    print("\nProcessing output...")
    doctags_doc = DocTagsDocument.from_doctags_and_image_pairs([output], [pil_image])
    doc = DoclingDocument.load_from_doctags(doctags_doc, document_name="Image Document")

    output_path = Path(args.output)
    ext = output_path.suffix.lower()

    if ext == ".md":
        output_path.write_text(doc.export_to_markdown())
    elif ext == ".xml":
        output_path.write_text(doc.export_to_doctags())
    elif ext == ".html":
        doc.save_as_html(output_path, image_mode=ImageRefMode.EMBEDDED)
    else:
        raise ValueError(f"Unsupported output extension: {ext!r} (use .md, .xml, or .html)")

    print(f"\nOutput saved to: {output_path}")

    if args.showInBrowser and ext == ".html":
        webbrowser.open(f"file:///{str(output_path.resolve())}")


if __name__ == "__main__":
    main()
