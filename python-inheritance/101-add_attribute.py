#!/usr/bin/python3
"""Defines a function that adds an attribute to an object when possible."""


def add_attribute(obj, name, value):
    """Add a new attribute to obj if obj supports it.

    Args:
        obj: the object to modify.
        name: the name of the new attribute.
        value: the value of the new attribute.

    Raises:
        TypeError: if obj cannot accept new attributes.
    """
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
