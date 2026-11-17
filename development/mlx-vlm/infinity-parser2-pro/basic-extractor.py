from PIL import Image
from mlx_vlm import load, generate
from mlx_vlm.prompt_utils import apply_chat_template

# Load the model and processor
model, processor = load("/Users/dden/.omlx/models/Infinity-Parser2-Pro-oQ4e")

# Build the messages for the model
pil_image = Image.open("./data/tiger-loop-01.png").convert("RGB")
min_pixels = 2048  # 32 * 64
max_pixels = 16777216  # 4096 * 4096
prompt = """
- Extract layout information from the provided PDF image.
- For each layout element, output its bbox, category, and the text content within the bbox.
- Bbox format: [x1, y1, x2, y2].
- Allowed layout categories: ['header', 'title', 'text', 'figure', 'table', 'formula', 'figure_caption', 'table_caption', 'formula_caption', 'figure_footnote', 'table_footnote', 'page_footnote', 'footer'].
- Text extraction and formatting:
  1) For 'figure', the text field must be an empty string.
  2) For 'formula', format text as LaTeX.
  3) For 'table', format text as HTML.
  4) For all other categories (e.g., text, title), format text as Markdown.
- The output text must be exactly the original text from the image, with no translation or rewriting.
- Sort all layout elements in human reading order.
- Final output must be a single JSON object.
"""

text = apply_chat_template(
    processor,
    model.config,
    prompt,
    num_images=1,
    enable_thinking=False,
)

# Generate the response
result = generate(
    model=model,
    processor=processor,
    prompt=text,
    image=pil_image,
    max_tokens=32768,
    temperature=0.0,
    top_p=1.0,
    min_pixels=min_pixels,
    max_pixels=max_pixels,
)

print(result.text)
