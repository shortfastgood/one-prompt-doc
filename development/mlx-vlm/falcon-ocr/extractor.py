import argparse

from mlx_vlm import load
from mlx_vlm.models.falcon_ocr import generate_with_layout

parser = argparse.ArgumentParser(description="Extract layout regions from an image with Falcon-OCR.")
parser.add_argument("--model", default="tiiuae/Falcon-OCR", help="The LLM to use (default: tiiuae/Falcon-OCR).")
parser.add_argument("--image", required=True, help="The image to scan (mandatory).")
parser.add_argument("--max-tok", type=int, default=8192, help="Maximum number of output tokens (default: 8192).")
parser.add_argument("--output", help="Write the output to this file instead of standard output.")
args = parser.parse_args()

model, processor = load(args.model)

regions = generate_with_layout(model, processor, image=args.image, max_tokens=args.max_tok)

lines = []
lines.append("| Category | Score | BBox | Text |")
lines.append("|----------|-------|------|------|")
for region in regions:
    text = region.get("text", "").replace("<|end_of_query|>", "")
    lines.append(f"| {region['category']} | {region.get('score', '')} | {region.get('bbox', '')} | {text} |")

if args.output:
    with open(args.output, "w") as f:
        f.write("\n".join(lines) + "\n")
else:
    print("\n".join(lines))