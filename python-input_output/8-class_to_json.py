#!/usr/bin/python3
"""Defines a class-to-dictionary conversion function."""


def class_to_json(obj):
    """Return the dictionary description of an object for JSON serialization.

    Args:
        obj: An instance of a class whose attributes are all serializable
            (list, dictionary, string, integer or boolean).

    Returns:
        dict: A dictionary holding the object's instance attributes.
    """
    return obj.__dict__.copy()
