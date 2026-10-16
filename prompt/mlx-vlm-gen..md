# mlx_vlm_gen.py

The utility examines the image. The utility reads the text from the image. The utility writes the text to the output file.

The utility has 4 arguments:

- --model: The AI model that you use. Default is mlx-community/DeepSeek-OCR-2-bf16.
- --image: The path to the image.
- --prompt: The prompt for the AI. Default is "<|grounding|>Convert the document to markdown.".
- --max-tokens: The limit for the number of tokens. Default is 8192.
- --output: The path to the output file. Default is output.md.

## Procedure

1. USE the environment /Users/dden/gitroot/one-prompt-doc/development/mlx-vlm/.venv.
2. USE the Python language.
3. USE example.py as the template.
4. PUT the result in the ./development/mlx-vlm folder.
5. IF a library is not installed, INSTALL the library.
6. WRITE the file requirements.txt in the ./development/mlx-vlm folder.