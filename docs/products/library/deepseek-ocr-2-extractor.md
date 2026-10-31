---
type: Program Overview
title: DeepSeek-OCR-2 image-to-markdown extractor
description: Behaviour and usage of development/mlx-vlm/deepseek-ocr-2/extractor.py.
tags: [ocr, mlx-vlm, deepseek-ocr-2, image, markdown]
sources:
  - id: extractor-source
    resource: /references/extractor.py.txt
    title: extractor.py, development/mlx-vlm/deepseek-ocr-2/
status: stable
generated:
  by: process:<author>
  at: 2026-10-30T16:30:00Z
---
# DeepSeek-OCR-2 image-to-markdown extractor

The script `development/mlx-vlm/deepseek-ocr-2/extractor.py` reads a single
document image (a PDF page also works as input) and converts it to Markdown
using the `mlx-community/DeepSeek-OCR-2-bf16` multimodal model through the
`mlx-vlm` runtime on Apple Silicon / Metal.[^extractor-source]

## What it does

1. Loads the model and its processor with `mlx_vlm.load`.
2. Formats the prompt with `apply_chat_template`, treating the input as one
   image.
3. Generates Markdown with `mlx_vlm.generate` at `temperature=0`.
4. Writes the result to a file (default `output.md`).
5. Prints the byte count, the generated token count, and the tokens/second
   throughput.

## Command-line interface

| Argument | Default | Notes |
| --- | --- | --- |
| `--model` | `mlx-community/DeepSeek-OCR-2-bf16` | The model to run. |
| `--image` | required | Path to the image (or PDF page) to analyze. |
| `--prompt` | `<|grounding|>Convert the document to markdown.` | The prompt for the model. |
| `--max-tokens` | `8192` | Upper limit on generated tokens. |
| `--output` | `output.md` | Where the Markdown is written. |
| `--trace` | off | Also prints the result text to standard output. |

## How the environment and DeepSeek-OCR-2 disagree

The checkpoint ships custom modeling code written for `transformers` 4.46,
while the installed `mlx-vlm` 0.7.8 depends on `transformers` 5.x. Two symbols
that the code imports were removed in `transformers` 5.x, so the import fails
before inference starts. The script patches this at runtime; the full rationale
is in [DeepSeek-OCR-2 environment patch](/deepseek-ocr-2-environment-patch.md).

> The script calls `_patch_missing_transformers_symbols()` once, before
> `load`. Without it, running the script with the supported versions raises an
> `ImportError` from the checkpoint's custom code.

## Dependencies

`mlx-vlm` and `torch>=2.5.0` (see `development/mlx-vlm/deepseek-ocr-2/requirements.txt`).
`mlx-vlm` pulls in `mlx`, `Pillow`, `numpy`, `safetensors`, and
`huggingface_hub`; `torch` is required explicitly because the script imports it
and `transformers` imports it at module load.

[^extractor-source]: Source copy kept as [`references/extractor.py.txt`](references/extractor.py.txt), mirroring `development/mlx-vlm/deepseek-ocr-2/extractor.py` at generation time.
