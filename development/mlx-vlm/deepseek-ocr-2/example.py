from mlx_vlm import load, generate
from mlx_vlm.prompt_utils import apply_chat_template

model, processor = load("mlx-community/DeepSeek-OCR-2-bf16")

prompt = "<|grounding|>Convert the document to markdown."
formatted_prompt = apply_chat_template(processor, model.config, prompt, num_images=1)

result = generate(
    model=model,
    processor=processor,
    image="paper.pdf",  # Also works with PDF pages
    prompt=formatted_prompt,
    max_tokens=2000,
    temperature=0.0,
)
print(result.text)