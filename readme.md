# Tetris

## Installation
Use python 3.11+

> using pyenv for managing python version and a virtual env for isolated dev environment

*Optional steps:*
```bash
pyenv local 3.11
python -m venv env
source env/bin/activate
```

install the packages

```bash
pip install -r requirements.txt
```

## Run the project
```bash
python main.py
```

## To update the alphabet
modify line 30 of the `constants.py` file add all the letter you want separated by space
for example:
```python
ALPHABET = 'c a t e b'. split()
```

To adjust the word list you can change line 6 of the `tetris.py` file
```python
def is_english_word(word):
    return word.lower() in ['cat', 'cut']
```
Te above code will only accept cat or cut as the words

