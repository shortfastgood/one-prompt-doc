# one-prompt-doc

This project deals with the extraction of text, with a particular focus on the extraction of text from an image. The aim is a procedure that does more than extract the text accurately. It should also preserve the internal organisation of the original document, such as titles, sections, and paragraphs. Ideally, the extracted material should also keep the information about the presence of images, charts, and tables.

To give the extraction a structure, a format is needed that keeps the organisation as well as the text. The format that suits this purpose best is [DocLang](https://doclang.ai), which was designed to be a format suitable for use with artificial intelligence.

On the open market there are OCR software packages (Optical Character Recognition) that do the extraction of text from images very well, such as [Tesseract OCR](https://github.com/tesseract-ocr/tesseract). There are also projects like [EasyOCR](https://github.com/JaidedAI/EasyOCR) and [PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR) that use artificial intelligence, but they all still need a large amount of code, mostly written in Python.

The same is true of the software packages that convert documents between different formats, such as [anydoc](https://crates.io/crates/anydoc) or [textract](https://textract.readthedocs.io/en/stable/).

Given the skills that artificial intelligence has reached in processing text in many languages and in processing and recognising images, an alternative way is to do the recognition or transformation of documents using mainly artificial intelligence and to keep the code written in languages like Python, Java, Rust, and C++ to a secondary role.

**Disclaimer**: The content and ideas expressed in this project are those of the author, but some parts are generated, in part or in full, by artificial intelligence. The texts are reviewed to ensure linguistically correct wording, with the support of AI.

## Prompt Engineering

Artificial intelligence is driven by instructions that specify the task and its context. The starting point is the frontier models and the agents that their makers supply with services for users. Four of these are considered: Claude Code (CLI and VSCode plugin), Codex (VSCode plugin), GitHub Copilot, and Mistral Vibe (VSCode plugin).

All of these agents read a configuration file (AGENTS.md or CLAUDE.md) that holds the development guidelines, inspired by the rules proposed by Andrej Karpathy.

| Principle | Addresses |
|-----------|-----------|
| **Think Before Coding** | Wrong assumptions, hidden confusion, missing tradeoffs |
| **Simplicity First** | Overcomplication, bloated abstractions |
| **Surgical Changes** | Orthogonal edits, touching code you shouldn't |
| **Goal-Driven Execution** | Leverage through tests-first, verifiable success criteria |

The guidelines alone are not enough; it is necessary to define the procedure for extracting from an image and transforming the result into a DocLang document. To achieve this, three [skills](https://support.claude.com/en/articles/12512176-what-are-skills) have been added to the project: ASD-STE100, DocLang, and LLMWiki.

### ASD-STE100 Skill

On 2 October 2026, Andrej Karpathy suggested in a [post on X](https://x.com/karpathy/status/2105819303471976479?s=20) to write specifications using the ASD-STE100 format, a controlled subset of the English language used in the aerospace industry. The purpose is to simplify the language and make it precise. The project uses the SKILL everywhere a precise and concise specification or prompt is required.

[Skill Documentation](./docs/products/asd-set100-skill/index.md)

### DocLang Skill

This skill is the fulfilment of what the project sets out to do: to replace code with a specification that, combined with artificial intelligence, delivers accurate text extraction from an image while preserving its internal organisation. The skill is based on version 0.8 of DocLang.

[Skill Documentation](./docs/products/doclang-skill/index.md)

### LLMWiki

This skill is used to manage the documentation of the project, organised as an [LLMWiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) in the OKF format ([Open Knowledge Format](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md) 0.2).

[Skill Documentation](./docs/products/llmwiki-skill/index.md)

## Environment

### Agent

- Antigravity CLI (former Gemini CLI)
- Claude Code (VSCode plugin and CLI), the desktop is not used because requires a subscription and doesn't work with API keys.
- Codex (VSCode plugin)
- GitHub Copilot (VSCode integration)
- Mistal Vibe (VSCode plugin)

### Local Engines

- [Ollama](https://ollama.com)
- [oMLX] (https://omlx.ai)
- [Slotstream](https://github.com/carloslfu/slotstream)

## Framework

- [Docling](https://github.com/docling-project/docling)
- [MLX-VLM](https://github.com/Blaizzy/mlx-vlm)

### Deepseek-OCR-2 dedicated script

- [Extractor documentation](./docs/products/library/deepseek-ocr-2-extractor.md)
- [Environment patch](./docs/products/library/deepseek-ocr-2-environment-patch.md)

## Test Cases

[Summary](./test/test-results.md)