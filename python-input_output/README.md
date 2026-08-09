# Python - Input/Output

ALX / Holberton higher-level programming project covering file reading and
writing, JSON serialization and deserialization, and stdin log parsing.

## Requirements

- Ubuntu 20.04 LTS, `python3` (3.8.x)
- All files end with a new line and start with `#!/usr/bin/python3`
- All files are PEP 8 compliant (`pycodestyle` 2.7.*)
- All modules, classes and functions carry a real docstring
- Only the JSON tasks import a module (`json`), plus `sys` where argv or
  stdin is needed

## Files

| File | Description |
| --- | --- |
| `0-read_file.py` | Reads a UTF-8 text file and prints it to stdout |
| `1-write_file.py` | Writes a string to a file, returns the char count |
| `2-append_write.py` | Appends a string to a file, returns the char count |
| `3-to_json_string.py` | Returns the JSON string for an object |
| `4-from_json_string.py` | Returns the object for a JSON string |
| `5-save_to_json_file.py` | Writes an object to a file as JSON |
| `6-load_from_json_file.py` | Creates an object from a JSON file |
| `7-add_item.py` | Adds argv items to a list in `add_item.json` |
| `8-class_to_json.py` | Returns the dict description of an instance |
| `9-student.py` | `Student` class with `to_json` |
| `10-student.py` | `Student` class with attribute filtering |
| `11-student.py` | `Student` class with `reload_from_json` |
| `12-pascal_triangle.py` | Returns Pascal's triangle of `n` |
| `100-append_after.py` | Inserts text after each matching line in a file |
| `101-stats.py` | Reads stdin and computes log metrics |

## Running

```
./0-main.py
./7-add_item.py Best School
./12-main.py
./101-generator.py | ./101-stats.py
```
