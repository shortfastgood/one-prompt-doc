"""Analyze an image and extract text from it with mlx-vlm (Apple/Metal).

Modeled on example.py (DeepSeek-OCR-2 document-to-markdown pipeline).
"""

import argparse

from mlx_vlm import load, generate
from mlx_vlm.prompt_utils import apply_chat_template


def _patch_missing_transformers_symbols() -> None:
    """Restore transformers 4.46-era symbols the model's custom code imports.

    The mlx-community DeepSeek-OCR-2 checkpoint ships custom modeling code
    (written for transformers 4.46) whose ``auto_map`` routes ``AutoConfig`` into
    a torch-based module that imports two symbols removed in transformers 5.x,
    which mlx-vlm 0.7.8 requires:

    * ``LlamaFlashAttention2`` (from ``modeling_llama``): flash-attention 2 is
      not active on Metal, so aliasing it to ``LlamaAttention`` is safe. It only
      appears in the model's attention registry and is never instantiated on this
      path.
    * ``is_torch_fx_available`` (from ``utils.import_utils``): only guards a
      ``torch.fx.wrap`` call, a graph-tracing optimization that has no effect on
      normal inference, so returning False is behavior-preserving.
    """
    try:
        import transformers.models.llama.modeling_llama as llama
    except ImportError:
        llama = None
    if llama is not None and not hasattr(llama, "LlamaFlashAttention2"):
        if hasattr(llama, "LlamaAttention"):
            llama.LlamaFlashAttention2 = llama.LlamaAttention

    try:
        import transformers.utils.import_utils as import_utils
    except ImportError:
        return
    if not hasattr(import_utils, "is_torch_fx_available"):
        import torch
        import_utils.is_torch_fx_available = lambda *args, **kwargs: (
            hasattr(torch, "fx")
        )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Analyze an image and extract its text with mlx-vlm."
    )
    parser.add_argument(
        "--model",
        default="mlx-community/DeepSeek-OCR-2-bf16",
        help="The AI model to use. Default: mlx-community/DeepSeek-OCR-2-bf16.",
    )
    parser.add_argument(
        "--image",
        required=True,
        help="Path to the image to analyze.",
    )
    parser.add_argument(
        "--prompt",
        default="<|grounding|>Convert the document to markdown.",
        help="The prompt for the AI.",
    )
    parser.add_argument(
        "--max-tokens",
        type=int,
        default=8192,
        help="Limit for the number of generated tokens. Default: 8192.",
    )
    parser.add_argument(
        "--output",
        default="output.md",
        help="Path to the output file. Default: output.md.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    _patch_missing_transformers_symbols()

    model, processor = load(args.model)

    formatted_prompt = apply_chat_template(
        processor, model.config, args.prompt, num_images=1
    )

    result = generate(
        model=model,
        processor=processor,
        image=args.image,
        prompt=formatted_prompt,
        max_tokens=args.max_tokens,
        temperature=0.0,
    )
    with open(args.output, "w", encoding="utf-8") as f:
        f.write(result.text)
    print(result.text)


if __name__ == "__main__":
    main()
