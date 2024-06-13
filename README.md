# Jupyter Notebook Translator

[![GitHub stars](https://img.shields.io/github/stars/fernandocarazomelo/jupyter-notebook-translator.svg?style=social&label=Star)](https://github.com/fernandocarazomelo/jupyter-notebook-translator)

Easily translate your Jupyter Notebooks from English or any other language to any language with this powerful tool. Designed for data scientists, researchers, and educators who want to make their work accessible to a native-speaking audience.

For details refer to the [py-googletrans API Documentation](https://py-googletrans.readthedocs.io/en/latest/). See available languages at the end of this README.

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

2. Create a virtual environment:

    ```sh
    python -m venv venv_notebook_translator
    source venv_notebook_translator/bin/activate
    ```

3. Install the required dependencies:

    ```sh
    pip install .
    ```

## Usage

### Help

To see the available commands and options, run:

```sh
python translate_notebook --help
```

### Translate a Single Notebook

To translate a single Jupyter Notebook:

```sh
python translate_notebook --input-path "./example/nb_en.ipynb" --output-path "./example/nb_es.ipynb" --output-language "es"
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


## Languages

| Language Code | Language Name          |
|---------------|------------------------|
| af            | afrikaans              |
| sq            | albanian               |
| am            | amharic                |
| ar            | arabic                 |
| hy            | armenian               |
| az            | azerbaijani            |
| eu            | basque                 |
| be            | belarusian             |
| bn            | bengali                |
| bs            | bosnian                |
| bg            | bulgarian              |
| ca            | catalan                |
| ceb           | cebuano                |
| ny            | chichewa               |
| zh-cn         | chinese (simplified)   |
| zh-tw         | chinese (traditional)  |
| co            | corsican               |
| hr            | croatian               |
| cs            | czech                  |
| da            | danish                 |
| nl            | dutch                  |
| en            | english                |
| eo            | esperanto              |
| et            | estonian               |
| tl            | filipino               |
| fi            | finnish                |
| fr            | french                 |
| fy            | frisian                |
| gl            | galician               |
| ka            | georgian               |
| de            | german                 |
| el            | greek                  |
| gu            | gujarati               |
| ht            | haitian creole         |
| ha            | hausa                  |
| haw           | hawaiian               |
| iw            | hebrew                 |
| he            | hebrew                 |
| hi            | hindi                  |
| hmn           | hmong                  |
| hu            | hungarian              |
| is            | icelandic              |
| ig            | igbo                   |
| id            | indonesian             |
| ga            | irish                  |
| it            | italian                |
| ja            | japanese               |
| jw            | javanese               |
| kn            | kannada                |
| kk            | kazakh                 |
| km            | khmer                  |
| ko            | korean                 |
| ku            | kurdish (kurmanji)     |
| ky            | kyrgyz                 |
| lo            | lao                    |
| la            | latin                  |
| lv            | latvian                |
| lt            | lithuanian             |
| lb            | luxembourgish          |
| mk            | macedonian             |
| mg            | malagasy               |
| ms            | malay                  |
| ml            | malayalam              |
| mt            | maltese                |
| mi            | maori                  |
| mr            | marathi                |
| mn            | mongolian              |
| my            | myanmar (burmese)      |
| ne            | nepali                 |
| no            | norwegian              |
| or            | odia                   |
| ps            | pashto                 |
| fa            | persian                |
| pl            | polish                 |
| pt            | portuguese             |
| pa            | punjabi                |
| ro            | romanian               |
| ru            | russian                |
| sm            | samoan                 |
| gd            | scots gaelic           |
| sr            | serbian                |
| st            | sesotho                |
| sn            | shona                  |
| sd            | sindhi                 |
| si            | sinhala                |
| sk            | slovak                 |
| sl            | slovenian              |
| so            | somali                 |
| es            | spanish                |
| su            | sundanese              |
| sw            | swahili                |
| sv            | swedish                |
| tg            | tajik                  |
| ta            | tamil                  |
| te            | telugu                 |
| th            | thai                   |
| tr            | turkish                |
| uk            | ukrainian              |
| ur            | urdu                   |
| ug            | uyghur                 |
| uz            | uzbek                  |
| vi            | vietnamese             |
| cy            | welsh                  |
| xh            | xhosa                  |
| yi            | yiddish                |
| yo            | yoruba                 |
| zu            | zulu                   |


