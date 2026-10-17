# mlx_vlm_gen.py

The utility examines the image. The utility reads the text from the image. The utility writes the text to the output file.

The utility has 6 arguments:

- --model: The AI model that you use. The default is mlx-community/DeepSeek-OCR-2-bf16.
- --image: The path to the image.
- --prompt: The prompt for the AI. The default is "<|grounding|>Convert the document to markdown.".
- --max-tokens: The limit for the number of tokens. The default is 8192.
- --output: The path to the output file. The default is output.md.
- --trace: IF THE FLAG IS ON, THE UTILITY WRITES ADDITIONALLY ON STANDARD OUTPUT. IF NOT, THE UTILITY DOES NOT WRITE ADDITIONALLY. THE DEFAULT IS OFF.

## Procedure

1. USE the environment /Users/dden/gitroot/one-prompt-doc/development/mlx-vlm/.venv.
2. USE the Python language.
3. USE example.py as the template.
4. At the end, WRITE the number of bytes written.
5. At the end, WRITE the number of output tokens IF THE DATA IS AVAILABLE.
6. At the end, WRITE the performance (tokens/second) IF ANY DATA IS AVAILABLE.
7. PUT the result in the ./development/mlx-vlm folder.
8. IF A LIBRARY IS NOT INSTALLED, INSTALL THE LIBRARY.
9. WRITE the file requirements.txt in the ./development/mlx-vlm folder.