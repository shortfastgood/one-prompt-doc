# Test Summary and Technical Notes

## Case Tiger Loop

| Number | Image | Model | Agent | Engine | Cost |
|--------|-------|-------|-------|--------|-------|
| 1 | tiger-loop-01.png | GPT-6 Astra (high) | Codex (VSCode plugin, 26.1021.22027) | OpenAI API | Included in my $20 flat rate subscription. |
| 2 | tiger-loop-01.png | Claude Sonnet 5.5 (high) | GitHub Copilot 1.143 | Anthropic API | $1.36, Token In 644765, Token Out 6573 |
| 3 | tiger-loop-01.png | Gemini 3.8 Flash (high) | Antigravity CLI 1.4.8 | Google API | Free starter quota. |
| 4 | tiger-loop-01.png | Mistral Medium 3.5 (high) | Mistral Vibe 1.27.0 | Mistral AI API | $0.32 included in a free account with a $10 flat rate |
| 5 | tiger-loop-01.png | Qwen 3.8 Flash Next 4Bit (high) | Claude Code (VSCode) 2.1.312 | Slotstream 0.2.30 | -- |
| 6 | tiger-loop-01.png | Qwen 3.8 27B 4Bit | Claude Code (CLI) 2.1.308 | oMLX 0.72 | -- |
| 7 | tiger-loop-01.png | Ornith 1.5 35b | GitHub Copilot 1.143 | Ollama 0.40.13 | -- |
| 8 | tiger-loop-01.png | Deepseek OCR 2 | python extractor script | mlx-vlm 0.7.11 | -- |


Notes:

1. **Full text extraction and a complete description of the scanned document.** The model describes the content of the embedded figures, images and tables correctly. This is a very good result, suitable for comparison. My flat rate subscription does not allow enough requests to extract a multi-page document in a short time frame. Using the API would make the cost per extracted page too high.

2. A fair comparison between Anthropic and OpenAI would require Fable 5, but with Sonnet 5.5 a single-page extraction costs $1.36, which is too costly to base an extraction pipeline on. Fable would increase the cost and, even with a result similar to Astra, is not worth it. The core meaning is preserved.

- [Extraction Report](./claude-sonnet-5.5-high/extraction_report.md)
- [DocLang](./claude-sonnet-5.5-high/tiger-loop-01.xml)

3. The agent attempts to use Tesseract (not installed) and reads additional files of the project, including existing results. If the extraction is genuinely done by Gemini, the result matches Astra. I dismiss the discovery, even if Gemini really produced it, because although the result is very good, a multi-page extraction pipeline would require an expensive subscription.

- [Extraction Report](./gemini-3.8-flash-high/extraction_report.md)
- [DocLang](./gemini-3.8-flash-high/tiger-loop-01.xml)

4. Clean result.

- [Extraction Report](./mistral-medium-3.5-high/extraction_report.md)
- [DocLang](./mistral-medium-3.5-high/tiger-loop-01.xml)

5. The word "burner" is replaced by "pump", changing the meaning of the relevant sentence. Although it is a single error, this shows that the model cannot be regarded as reliable. The recognition of the main table also falls short of expectations. Additionally, the execution is very long.

- [Extraction Report](./qwen3.8-flash-next-4bit-high/extraction_report.md)
- [DocLang](./qwen3.8-flash-next-4bit-high/tiger-loop-01.xml)

6. The text recognition mistook a comma for a full stop, splitting one sentence into two. The meaning does not change, but the tendency to make small yet decisive errors is present. The result contains the coordinates of images, tables and text, but the structure is far more simplified than in the reference. Here the processing takes the user up to 60 minutes for the extraction and validation of the result. The semantics is not compromised. A quick comparison test with a graphics editor showed that the coordinates are unreliable, and that a resolution of 512×512 is declared, which is entirely incorrect.

- [Extraction Report](./qwen3.8-27b-mlx-4bit/extraction_report.md)
- [DocLang](./qwen3.8-27b-mlx-4bit/tiger-loop-01.xml)

7. The recognition was one of the fastest, at around 18 minutes, but at the cost of a few errors that do not compromise the semantics. The subsequent attempt at correction proved unsatisfactory: 40 minutes were spent correcting the errors mentioned in the prompt, while those not mentioned were ignored.

- [Extraction Report](./ornith-1.5-35b/1_extraction_report.md)
- [Correction Report](./ornith-1.5-35b/2_correction_report.md)
- [DocLang](./ornith-1.5-35b/tiger-loop-01.xml)

8. The extraction takes a few seconds, but it is limited to the text. The images embedded in the image are recorded as images and are not scanned. However, the semantics is respected, as is the reading order. In this case, as it is a specialised model, neither AGENT.md nor skills are used. The output is not in DocLang format but in Markdown format.

- [Extraction Report](./deepseek-ocr-2/extraction_report.md)
- [Markdown](./deepseek-ocr-2/tiger-loop-01.md)
