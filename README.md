# Jupyter Notebook Translator

[![GitHub stars](https://img.shields.io/github/stars/fernandocarazomelo/jupyter-notebook-translator.svg?style=social&label=Star)](https://github.com/fernandocarazomelo/jupyter-notebook-translator)

Easily translate your Jupyter Notebooks from English to Spanish with this powerful tool. Designed for data scientists, researchers, and educators who want to make their work accessible to a Spanish-speaking audience.

## Features

- Translate entire Jupyter Notebooks with a single command.
- Translate only the comments in your code cells.
- Supports batch processing of multiple notebooks in a directory.
- Simple command-line interface (CLI) powered by [typer](https://github.com/tiangolo/typer).
- Utilizes [googletrans](https://github.com/ssut/py-googletrans) for translation.

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/fernandocarazomelo/jupyter-notebook-translator.git
    cd jupyter-notebook-translator
    ```

2. Install the required packages:

    ```sh
    pip install -r requirements.txt
    ```

## Usage

### Translate a Single Notebook

To translate a single Jupyter Notebook:

```sh
python translate_notebook --input-path "./notebooks_english/nb_en.ipynb" --output-path "./notebooks_spanish/nb_es.ipynb"
```

### Translate All Notebooks in a Directory

To translate all notebooks in a directory:

```sh
python translate_notebook --input-path "./notebooks_english" --output-path "./notebooks_spanish"
```

## Examples

### Translating a Single Notebook

```sh
python main.py --input-path "./notebooks_english/example_notebook.ipynb" --output-path "./notebooks_spanish/example_notebook.ipynb"
```

### Translating an Entire Directory

```sh
python main.py --input-path "./notebooks_english" --output-path "./notebooks_spanish"
```

## Contributing

We welcome contributions! Please see our [CONTRIBUTING.md](CONTRIBUTING.md) for more details.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

If you encounter any issues or have any questions, feel free to open an issue on GitHub.

## Acknowledgments

- [googletrans](https://github.com/ssut/py-googletrans) for the translation engine.
- [typer](https://github.com/tiangolo/typer) for the CLI framework.

## Spread the Word!

If you find this project useful, please consider giving it a ⭐ on GitHub and sharing it with your friends and colleagues!

[![GitHub stars](https://img.shields.io/github/stars/fernandocarazomelo/jupyter-notebook-translator.svg?style=social&label=Star)](https://github.com/fernandocarazomelo/jupyter-notebook-translator)

```

### Additional Files

#### `requirements.txt`
Ensure you have a `requirements.txt` for the required dependencies.

```plaintext
typer[all]
googletrans==4.0.0-rc1
nbformat
```



