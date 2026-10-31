---
type: Program Overview
title: Docling image-to-document extractor (mlx)
description: Behaviour and usage of development/docling/extractor.py, which turns one page image into Markdown, DocTags XML, or HTML through the ibm-granite/granite-docling model.
tags: [docling, mlx-vlm, granite-docling, image, ocr, markdown, html]
sources:
  - id: docling-extractor-source
    resource: /references/docling-extractor.py.txt
    title: extractor.py, development/docling/
  - id: docling-requirements
    resource: /references/docling-requirements.txt
    title: requirements.txt, development/docling/
status: stable
generated:
  by: process:llmwiki
  at: 2026-10-31T12:14:36Z
---
# Docling image-to-document extractor (mlx)

The script `development/docling/extractor.py` reads one page image (a URL or a
local file, including a rendered PDF page) and converts it into a structured
document by running the `ibm-granite/granite-docling-258M-mlx` multimodal model
through the `mlx-vlm` runtime on Apple Silicon / Metal. It emits DocTags, which
the `docling-core` library turns into a `DoclingDocument` that can be exported as
Markdown, DocTags XML, or HTML.[^docling-extractor-source]

The script is the command-line, multi-format descendant of the reference example
`development/docling/example-mlx.py`, which runs the same model and DocTags
pipeline as a single-file demo.

## What it does

1. Loads the model and processor with `mlx_vlm.load`, and reads the model config
   with `mlx_vlm.utils.load_config`.
2. Loads the image (URL or path) with `transformers.image_utils.load_image` and
   formats the prompt with `apply_chat_template`, treating the input as one
   image.
3. Streams the model output with `mlx_vlm.stream_generate`, accumulating token
   text and stopping as soon as the closing `</doctag>` marker appears.
4. Builds a `DocTagsDocument` from the generated DocTags string and the image,
   then loads it into a `DoclingDocument` named `Image Document`.
5. Writes the document to `--output`, choosing the exporter by file extension,
   and (optionally) opens the result in a browser when the output is HTML.

## Command-line interface

| Argument | Default | Notes |
| --- | --- | --- |
| `--model` | `ibm-granite/granite-docling-258M-mlx` | The model to run. |
| `--image` | required | URL or path to the image (a rendered PDF page also works). |
| `--prompt` | `Convert this page to docling.` | The prompt for the model. |
| `--max-tokens` | `8192` | Upper limit on generated tokens. |
| `--output` | required | Where the result is written; the extension selects the format. |
| `--showInBrowser` | off | Open the result in the browser when the output is HTML. |
| `--trace` | off | Also write the generated DocTags to standard output as they stream. |

## Output formats

The exporter is chosen from the lowercased suffix of `--output`:

| Extension | Exporter | Result |
| --- | --- | --- |
| `.md` | `doc.export_to_markdown()` | Markdown text. |
| `.xml` | `doc.export_to_doctags()` | DocTags (XML) text. |
| `.html` | `doc.save_as_html(..., image_mode=ImageRefMode.EMBEDDED)` | Self-contained HTML with the image embedded. |

Any other extension raises a `ValueError` naming the three supported
extensions. The `--showInBrowser` flag has an effect only for `.html` output: it
opens `file:///<resolved path>` in the system browser.

## Dependencies

`docling-core`, `mlx-vlm`, `pillow`, and `transformers` (see
`development/docling/requirements.txt`).[^docling-requirements] The script also
declares a `requires-python = ">=3.12"` marker and the same dependency list in its
inline script header, so it can be run as a standalone PEP 723 script. Unlike the
[DeepSeek-OCR-2 extractor](/deepseek-ocr-2-extractor.md), this script relies on
the model's `auto_map` loading cleanly through the installed `mlx-vlm`, and so it
performs no `transformers` symbol patching.

[^docling-extractor-source]: Source copy kept as [`references/docling-extractor.py.txt`](references/docling-extractor.py.txt), mirroring `development/docling/extractor.py` at generation time.
[^docling-requirements]: Requirements copy kept as [`references/docling-requirements.txt`](references/docling-requirements.txt), mirroring `development/docling/requirements.txt` at generation time.
