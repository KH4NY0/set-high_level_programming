#!/usr/bin/python3
"""Defines a JSON file writing function."""
import json


def save_to_json_file(my_obj, filename):
    """Write an object to a text file using its JSON representation.

    Args:
        my_obj: The object to serialize.
        filename (str): The name of the file to write to.
    """
    with open(filename, "w", encoding="utf-8") as a_file:
        json.dump(my_obj, a_file)
