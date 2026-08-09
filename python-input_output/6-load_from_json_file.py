#!/usr/bin/python3
"""Defines a JSON file reading function."""
import json


def load_from_json_file(filename):
    """Create a Python object from a JSON file.

    Args:
        filename (str): The name of the JSON file to read.

    Returns:
        The Python data structure held in the file.
    """
    with open(filename, encoding="utf-8") as a_file:
        return json.load(a_file)
