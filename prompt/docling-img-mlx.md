# docling-img.py

The utility uses the Docling project to examine an image and read the text in the image.

The utility has 5 arguments:

- --model: The AI model to use. The default value is ibm-granite/granite-docling-258M-mlx.
- --image: The path to the image.
- --prompt: The prompt for the AI. The default value is "Convert this page to docling."
- --output: The path to the output file.
  - If the extension is .md, the format is Markdown.
  - If the extension is .xml, the output file contains the doc-tags.
  - If the extension is .html, the format is HTML.
- --showInBrowser: When the flag is on and the output format is HTML, the utility shows the result in the default browser.

## Procedure
1. Use the environment /Users/dden/gitroot/one-prompt-doc/development/docling/.venv.
2. Use the Python language.
3. Use example.py as the template.
4. Put the result in the development/docling folder.
5. If a library is not installed, install the library.
6. Write the file requirements.txt in the development/docling folder.