from googletrans import Translator
import nbformat


def translate_text(text, source_language, output_language):
    translator = Translator()
    return translator.translate(text, src=source_language, dest=output_language).text


def translate_code_only_comments_in_list(codes, source_language, output_language):
    translated_codes = []
    for code in codes:
        lines = code.splitlines()
        translated_code = []
        for line in lines:
            if line.startswith("#"):
                translated_comment = translate_text(
                    line[1:].strip(), source_language, output_language
                )
                translated_code.append("# " + translated_comment)
            else:
                translated_code.append(line)
        translated_codes.append("\n".join(translated_code))
    return translated_codes


def translate_notebook(input_path, output_path, source_language, output_language):
    # Read the original notebook
    with open(input_path, "r", encoding="utf-8") as notebook_file:
        notebook_content = notebook_file.read()
    notebook = nbformat.reads(notebook_content, as_version=4)

    # Translate the text content
    text_content = [
        cell.source for cell in notebook.cells if cell.cell_type == "markdown"
    ]
    translated_text = [
        translate_text(text, source_language, output_language) for text in text_content
    ]

    # Translate the code content
    code_content = [cell.source for cell in notebook.cells if cell.cell_type == "code"]
    translated_code = translate_code_only_comments_in_list(
        code_content, source_language, output_language
    )

    # Create a new notebook
    new_notebook = nbformat.v4.new_notebook()

    # Add translated cells to the new notebook
    for cell in notebook.cells:
        if cell.cell_type == "markdown":
            new_notebook.cells.append(
                nbformat.v4.new_markdown_cell(translated_text.pop(0))
            )
        elif cell.cell_type == "code":
            new_notebook.cells.append(nbformat.v4.new_code_cell(translated_code.pop(0)))
        else:
            new_notebook.cells.append(cell)

    # Write the new notebook to a file
    if output_path == "":
        output_path = input_path.replace(".ipynb", "_translated.ipynb")
    with open(output_path, "w", encoding="utf-8") as f:
        nbformat.write(new_notebook, f)

    print(f"Translated notebook saved to: {output_path}")
