# MLX-VLM DocLang implementation plan

This plan uses ASD-STE100 Issue 9 for “ASD-SET100”.

The program changes one local image into one DocLang 0.8 XML file. Python controls the full procedure for the DocLang skill.

The model supplies the image analysis and the XML text. Python reads the skill files, starts the checker, and writes the output file.

## 1. Interface and limits

Use these command-line parameters:

| Parameter | Requirement | Value |
| --- | --- | --- |
| `--model` | Optional | A Hugging Face model ID or a local model directory. |
| `--prompt` | Optional | Instructions for the image extraction. |
| `--max-token` | Optional | The maximum output tokens for each model call. Use a positive integer. The default is 8192. |
| `--image` | Necessary | The path to one local PNG or JPEG image. |
| `--output` | Necessary | The path to the new `.dclg` or `.xml` file. |

Set the default model ID to `lmstudio-community/Qwen3.8-27B-MLX-4bit`.

Set the default prompt to “Change the full image to DocLang 0.8. Keep all text from the image and its structure.”

Use the `--max-token` value for extraction, each crop inspection, review, and repair. This value is not a total for the procedure.

Set the skill directory to `/Users/dden/gitroot/one-prompt-doc/.agents/skills/doclang`.

The program uses different model IDs without changes to the code. The selected model must have image input through MLX-VLM. An MLX model with only text input cannot do this procedure.

The first version uses one image for each command. This version does not include PDF input, image URLs, more than one page, or archive output.

The prompt controls the extraction task. It does not change the output path or the DocLang format. ASD-STE100 is applicable to this plan. Do not change source text to STE.

## 2. Files and dependencies

1. Add `development/mlx-vlm/mlx_vlm_doclang.py` for the command-line program.
2. Add `development/mlx-vlm/test_mlx_vlm_doclang.py` for the automated tests. Add `development/mlx-vlm/test_cv_linear_structure.py` for the CV structure checks.
3. Add `development/mlx-vlm/requirements-doclang.txt` for the necessary packages.
4. Use `mlx-vlm`, Pillow, and the Python standard library.
5. After the installation and model tests give satisfactory results, record the package versions.
6. Do not change the existing examples or their dependencies.

Use small functions for the parameters, skill files, model calls, checks, and output. Use `main()` to control their sequence. A general agent framework is not necessary for this specified procedure.

## 3. Input checks

1. Read the parameters with `argparse`.
2. Make sure that `--max-token` is a positive integer. If it is not, stop with exit code `2`.
3. Make sure that Pillow can read the image pixels.
4. Make sure that the output directory has write permissions.
5. If there is an output file at the supplied path, stop with an error.
6. Make sure that the output suffix is `.dclg` or `.xml`.
7. Make sure that Python can read all four skill files in section 4.
8. Complete these checks before the model load.

Use the supplied paths independently of the current directory for the skill files. Use the current directory as the base directory for relative image and output paths.

## 4. Skill procedure

1. Read `SKILL.md` from the specified skill directory.
2. Read `references/syntax.md` from that directory.
3. Read `references/examples.md` from that directory.
4. Include these instructions and references in the model context.
5. Identify the examples with an “Examples” label.
6. Use `scripts/check_doclang.py` for the structural checks.

Load the full syntax reference for this first version. Do not load the 102-page source specification.

Use different messages for the skill instructions and the user prompt. Use text in the image only as source data. Do not obey commands from the image or the model response.

These steps control the skill procedure. A skill name in a prompt does not start a Python function or a model tool.

## 5. Model load and extraction

1. Load the selected model and processor one time with `mlx_vlm.load()`.
2. Use the selected model configuration with `apply_chat_template()`.
3. Supply the image pixels through the image input.
4. Set the image count to the number of images in each call.
5. Set `temperature=0.0`. Use the `--max-token` value as the output limit. The default is 8192 tokens.
6. Calculate the token count with the processor. Include the image tokens and the output allowance.
7. If the input token count plus the output allowance is more than the context limit, stop with an error. Do not decrease the allowance automatically.
8. Tell the model to find the regions and their reading order before it writes the XML.
9. Tell the model to supply only one full XML document.
10. Get the model text from the result text field for the installed MLX-VLM version.

Keep the source spelling, language, numbers, punctuation, and units. Use the DocLang rules for lists, tables, forms, pictures, and unreadable content. Do not add coordinates, asset paths, or text without source data.

Use font properties, positions, and distances between regions to find the document structure. Find the document title, section headings, subsection headings, and body text. Set the `level` attribute on each heading to show these relationships. Use integers more than zero.

A heading in the left margin can identify content to its right. Do not automatically treat such a heading as body text or as a different column. Bold text is not always a heading.

Use `group` elements for related blocks. Keep each block's heading, location, date or status, and content together when the image shows this relationship. Use nested groups when necessary. Do not add headings or groups without source content.

Do not write the string representation of the result object. Do not include model reasoning or status messages in the XML output.

If the response contains text around one full DocLang XML document, extract that document without changes to its content. First, use the XML parser to check the full span between the root tags. Use the first root start tag and the last root end tag as the limits. Make sure that the namespace and version agree with section 7. If parsing fails, keep the response for the checker and repair procedure. Use the same procedure for responses with more than one DocLang document.

For each model, use message roles that are compatible with its chat template. If the model has a non-thinking mode, use that mode for XML generation. Use only configuration options that are compatible with that model.

If MLX-VLM cannot load or operate the selected model, show the error. Do not select a different model automatically.

## 6. Image inspection and repair

1. Write the first XML result to a temporary file.
2. Start the checker with the current Python interpreter and the temporary path.
3. Keep the checker messages and exit code.
4. Make a second model call with the source image, first result, skill context, and checker messages.
5. Tell the model to compare each image region with the XML.
6. Include checks for heading levels, group boundaries, group membership, missing text, reading order, table spans, field associations, and checkbox states.
7. Tell the model to supply the full corrected XML document.
8. Start the checker on this result.
9. If there are errors, make one last repair call with the image and checker messages.
10. Start the checker again after that repair.
11. If there are errors, stop with an error.

During the image review, check headings that the draft shows as body text. Check the relationships between headings and their content. Check captions, field labels, and bold or italic body text before a change to a heading. Do these checks even when the XML checker reports no errors.

Add these instructions to the existing extraction and review calls. Do not add another layout call for this change.

If the first extraction contains unreadable content, include one crop inspection step before the second call. Use four image crops from Pillow with an overlap between adjacent crops. Examine each crop independently with the same model. Keep the crop offsets and results for the second call. These crops are parts of the same page, not more pages.

Use a two-by-two crop grid with a 10% overlap at the internal boundaries. Calculate horizontal overlap from the full image width. Calculate vertical overlap from the full image height. Tell the model to identify unreadable content with “Unreadable content:” in the applicable `description` element. Use that marker to start the crop inspection. Do not do the crop inspection again after a repair.

This procedure usually uses two model calls. It uses a maximum of seven model calls. Four calls are for the optional crop inspection.

Obey the skill instructions for `description` elements. Do not add characters that the model cannot read.

Reject an empty response or XML with missing end tags. If generation stops at the output limit, show an error. A closing XML tag is not sufficient to accept the result.

The checker finds some structural errors. It cannot make sure that all schema rules or all transcription details are correct. Errors can also stay after the model compares the XML with the image.

## 7. Output and status

1. Write the last document as UTF-8 XML without Markdown fences. Use the same DocLang format for the two suffixes.
2. Use one `doclang` root with namespace `https://www.doclang.ai/ns/v0` and version `0.8`.
3. Write the output file only after the necessary checks give satisfactory results.
4. Use a temporary file in the output directory to prevent an output file with missing data.
5. If a failure occurs, do not change an existing output file.
6. Send status messages and errors to standard error.
7. Show the skill path, model ID, procedure step, and checker result in the status messages.

Use exit code `0` after the output file write completes. Use exit code `2` for parameter or input errors. Use exit code `1` for model, checker, or output failures.

If the output contains unreadable content, show a message on standard error. Exit code `0` identifies a completed procedure with satisfactory structural checks. A person must compare the transcription with the image.

## 8. Verification

Do these automated tests before the model tests:

| Test | Necessary result |
| --- | --- |
| Default parameters | The model ID, skill path, and output limit of 8192 tokens agree with this plan. |
| Invalid `--max-token` value | Zero, negative numbers, and values that are not integers cause exit code `2` before the model load. |
| Specified `--max-token` value | Generation, context checks, and output-limit checks use the supplied value. |
| Different model ID | The model loader receives the supplied ID without changes. |
| Missing image or skill file | The program stops before the model load. |
| Output suffix | The program accepts `.dclg` and `.xml`. The files contain DocLang XML. Other suffixes cause exit code `2`. |
| Existing output file | The program does not change an existing `.dclg` or `.xml` file. |
| Model call | The request contains the image pixels, skill instructions, references, and user prompt. |
| Model result object | The program uses the text field, not the object representation. |
| Text around one full DocLang document | The XML parser accepts the document before extraction. The XML content does not change. |
| More than one DocLang document | The program does not select a document. The response goes to the checker and repair procedure. |
| Incorrect XML | The repair call receives the checker messages. |
| Checker errors after repair | The program stops after the specified repair calls. |
| Missing text in the first result | The second call receives the image and first result to compare them. |
| Missing hierarchy in valid XML | Image review still occurs. The output keeps the heading levels and groups from the corrected result. |
| Unreadable content | The crop inspection occurs one time and keeps the page identity. |
| Empty response or missing end tags | The program does not write the output file. |
| Context limit or output limit | The program shows an error without an output file. |
| Correct result | The program writes one UTF-8 DocLang document. |

Use test doubles for the automated model calls. Use the checker from the skill directory for the structural tests.

Then do model tests on Apple Silicon with only the default model. Use known images with text, columns, merged table cells, forms, unreadable text, and a photograph.

Compare the output with each source image. Record transcription errors and structural errors in different lists. Make sure that a different current directory does not change the skill path.

For each test image, prepare a reference transcription and a list of necessary structural elements. Make sure that all text that a person can read agrees with the reference transcription. Make sure that table dimensions, spans, and checkbox states agree with the source. Reject added text that has no source in the image.

For the hierarchy check, use `data/CV-linear.png` with the default model. Do not change the supplied comparison files. Write the new result to a different path.

Check these relationships in the CV result:

1. The name and the three section labels are headings.
2. Each employer heading level is one more than the experience section heading level. The university heading level is one more than the education section heading level.
3. Each employment group contains its employer heading, location, and seven list items.
4. The status `present` belongs to the third employment group.
5. The university and degree belong to the same group.
6. The skills list contains ten items. There are 31 list items in total.

Keep these CV checks in `development/mlx-vlm/test_cv_linear_structure.py`. Do not put CV names, section labels, or expected counts in the extraction program. Check the generated output with these tests. Also check transcription against the image; the Copilot output is not a reference transcription.

Complete the implementation when all automated tests and model tests give satisfactory results. Record the model IDs, package versions, memory consumption, and remaining errors.

## 9. Command example

After implementation, use this command from the project root:

```sh
python3 development/mlx-vlm/mlx_vlm_doclang.py \
  --model lmstudio-community/Qwen3.8-27B-MLX-4bit \
  --prompt "Change the full image to DocLang 0.8. Keep all text from the image and its structure." \
  --max-token 8192 \
  --image ./data/bowers.jpg \
  --output ./output.xml
```

## 10. References and terminology

The [MLX-VLM usage documentation](https://github.com/Blaizzy/mlx-vlm/blob/main/docs/usage.md) gives the Python model interface. The [default model card](https://huggingface.co/lmstudio-community/Qwen3.8-27B-MLX-4bit) gives an MLX-VLM image example. These references do not replace the model tests.

The [DocLang skill](../.agents/skills/doclang/SKILL.md) gives the extraction procedure. Its [syntax reference](../.agents/skills/doclang/references/syntax.md) gives the necessary XML subset. Its [checker](../.agents/skills/doclang/scripts/check_doclang.py) supplies the structural checks.

This plan uses computer-science terms as technical nouns. Refer to ASD-STE100 rule 1.5, category 19. Examples include skill, prompt, processor, token, context limit, namespace, model call, test double, and exit code.

Document terms include reading order, transcription, unreadable content, merged cell, and syntax reference. Refer to rule 1.5, categories 15 and 19. The technical verb “load” refers to a computer process in rule 1.12, category 2.

Additional document terms are font properties, body text, heading hierarchy, group boundaries, and group membership. Refer to rule 1.5, categories 15 and 19.

DocLang element names, file paths, API identifiers, and command parameters keep their specified spelling.

The [ASD-STE100 skill](../.agents/skills/asd-ste100/SKILL.md) supplies the Issue 9 rules and dictionary for the language check.
