#!/usr/bin/python3
"""Defines a function checking class membership, inheritance included."""


def is_kind_of_class(obj, a_class):
    """Return True if obj is an instance of a_class or of a subclass of it.

    Args:
        obj: the object to check.
        a_class: the class to compare against.

    Returns:
        True if obj is an instance of a_class or any subclass, else False.
    """
    return isinstance(obj, a_class)
