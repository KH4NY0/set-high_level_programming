#!/usr/bin/python3
"""Defines a function that lists the attributes and methods of an object."""


def lookup(obj):
    """Return the list of available attributes and methods of obj.

    Args:
        obj: the object to inspect.

    Returns:
        A list of attribute and method names.
    """
    return dir(obj)
