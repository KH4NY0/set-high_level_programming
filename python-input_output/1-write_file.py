#!/usr/bin/python3
"""Defines a text file writing function."""


def write_file(filename="", text=""):
    """Write a string to a UTF-8 text file.

    The file is created if it does not exist and overwritten if it does.

    Args:
        filename (str): The name of the file to write to.
        text (str): The text to write.

    Returns:
        int: The number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as a_file:
        return a_file.write(text)
