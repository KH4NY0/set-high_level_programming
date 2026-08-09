#!/usr/bin/python3
"""Defines a function that inserts text after matching lines in a file."""


def append_after(filename="", search_string="", new_string=""):
    """Insert ``new_string`` after every line containing ``search_string``.

    Args:
        filename (str): The name of the file to update.
        search_string (str): The string to look for in each line.
        new_string (str): The text to insert after each matching line.
    """
    updated = []
    with open(filename, encoding="utf-8") as a_file:
        for line in a_file:
            updated.append(line)
            if search_string in line:
                updated.append(new_string)

    with open(filename, "w", encoding="utf-8") as a_file:
        a_file.write("".join(updated))
