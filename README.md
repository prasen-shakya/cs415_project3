# Project 3: Tries (CS 415)

## Environment Set Up Guide

Create a virtual environment
```
python -m venv .venv
```

Activate the virtual environment
```
source .venv/bin/activate
```

Install dependencies
```
pip install -r requirements.txt
```

## Usage

```
python main.py <input_file> <flag>
```

- `input_file`: name of a text file inside the `input/` directory (e.g. `tale-1.txt`).
- `flag`:
  - `1`: interactive mode. Enter a search string to see search cost, autocomplete results, and autocomplete cost. Exit with Ctrl+C.
  - `2`: search every word in the file and report the total search cost.

Examples:

```
python main.py test.txt 1
python main.py tale-1.txt 2
```

## Tests
Run
```
pytest
```