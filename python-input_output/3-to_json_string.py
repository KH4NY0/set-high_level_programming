#!/usr/bin/python3
"""Defines a JSON serialization function."""
import json


def to_json_string(my_obj):
    """Return the JSON representation of an object as a string.

    Args:
        my_obj: The object to serialize.

    Returns:
        str: The JSON string representation of ``my_obj``.
    """
    return json.dumps(my_obj)
