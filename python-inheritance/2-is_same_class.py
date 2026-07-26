#!/usr/bin/python3
"""Defines a function checking for an exact class match."""


def is_same_class(obj, a_class):
    """Return True if obj is exactly an instance of a_class.

    Args:
        obj: the object to check.
        a_class: the class to compare against.

    Returns:
        True only if obj's type is a_class itself, False otherwise.
    """
    return type(obj) is a_class
