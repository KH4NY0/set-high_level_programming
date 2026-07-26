#!/usr/bin/python3
"""Defines a function checking for strict inheritance."""


def inherits_from(obj, a_class):
    """Return True if obj is an instance of a strict subclass of a_class.

    Args:
        obj: the object to check.
        a_class: the class to compare against.

    Returns:
        True if obj's class inherited from a_class, False if it is a_class.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
