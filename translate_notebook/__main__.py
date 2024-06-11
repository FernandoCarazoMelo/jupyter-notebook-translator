import typer
import os
from translator import translate_notebook

app = typer.Typer()


def translate_notebooks_in_directory(input_directory: str, output_directory: str):
    # Ensure the output directory exists
    os.makedirs(output_directory, exist_ok=True)

    # Iterate over all files in the input directory
    for filename in os.listdir(input_directory):
        if filename.endswith(".ipynb"):
            input_path = os.path.join(input_directory, filename)
            output_path = os.path.join(output_directory, filename)
            translate_notebook(input_path, output_path)
            print(f"Translated {filename} and saved to {output_path}")


@app.command()
def main(
    input_path: str = "./notebooks_english",
    output_path: str = "./notebooks_spanish",
):
    if os.path.isdir(input_path):
        translate_notebooks_in_directory(input_path, output_path)
    else:
        translate_notebook(input_path, output_path)


if __name__ == "__main__":
    app()
