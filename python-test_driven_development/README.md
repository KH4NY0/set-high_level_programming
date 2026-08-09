# Python - Test-driven development

ALX / Holberton higher-level programming project on test-driven development
in Python, using `doctest` and `unittest`.

## Requirements

- Ubuntu 20.04 LTS, `python3` (3.8.x)
- All files end with a new line and start with `#!/usr/bin/python3`
- All files are PEP 8 compliant (`pycodestyle` 2.7.*)
- All modules, classes and functions carry a real docstring
- No module may be imported, except in `101-lazy_matrix_mul.py` (NumPy)

## Files

| File | Description |
| --- | --- |
| `0-add_integer.py` | Adds two integers, casting floats first |
| `2-matrix_divided.py` | Divides every element of a matrix, rounded to 2 dp |
| `3-say_my_name.py` | Prints `My name is <first> <last>` |
| `4-print_square.py` | Prints a square of `#` characters |
| `5-text_indentation.py` | Prints text with 2 new lines after `.`, `?` and `:` |
| `6-max_integer.py` | Returns the largest value in a list (given) |
| `100-matrix_mul.py` | Multiplies two matrices without any module |
| `101-lazy_matrix_mul.py` | Multiplies two matrices with NumPy |

Tests live in `tests/`.

## Running the tests

Doctests:

```
python3 -m doctest -v ./tests/*.txt
```

Unittests:

```
python3 -m unittest tests.6-max_integer_test
```
