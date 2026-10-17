# one-prompt-doc

The purpose of this project is to study the conversion and extraction of text using artificial intelligence. Good software packages that do not use artificial intelligence already exist for the conversion between different formats and therefore also for the extraction, such as [textract](https://textract.readthedocs.io/en/stable/) or [MarkItDown](https://github.com/microsoft/markitdown).

## Framework

For photographed or scanned text, recognition has always been difficult and not always good. I began with the vLLM framework, but the support for macOS and Apple Silicon is not good enough. MLX-VLM, however, is more specific and easier to use.

A further help comes from the [Docling](https://github.com/docling-project/docling) project, which combines the use of artificial intelligence with the conversion to and from a large number of formats, including photographed and scanned documents.

## Prompt Engineering

On 2 October 2026, Andrej Karpathy suggests in a [post on X](https://x.com/karpathy/status/2105819303471976479?s=20) to write specifications using the ASD-STE100 format, a controlled subset of the English language used in the aerospace industry. The purpose is to simplify the language and make it precise. I had GPT-6 Astra generate a SKILL based on the asd-ste100-issue-9 specification. The SKILL contains not only the rules but also the dictionary. This may slow the execution, but I judged that the result is better when the aim is to obtain a text that follows the specification.

The SKILL needs a Python 3 interpreter that is installed and usable.

I made my first tests by asking it to convert the prompts that I had written to generate the simple demonstration utilities of this project.

## Models

For the generation and management of the project, where not stated otherwise, I use the latest versions of Qwen (currently 3.8 27b), Ollama (engine), GitHub Copilot (VSC plugin), and Claude Code. The purpose is to ensure local use of all the software, without depending on the outside.

### Deepseek-OCR-2

There is a dependency problem between mlx-vlm and the support files of the model. Qwen was still able to create a patch that solves the problem. These issues are common in fast-changing fields, but they waste time and do not allow a stable environment. Deepseek-OCR-2 is also relatively large, even though it is quite fast.