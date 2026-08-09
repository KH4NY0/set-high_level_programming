#!/usr/bin/python3
"""Defines an integer addition function.

This module exposes a single function, ``add_integer``, which adds two
numbers together after casting them to integers.
"""


def add_integer(a, b=98):
    """Return the integer addition of ``a`` and ``b``.

    Float arguments are typecast to integers before the addition.

    Args:
        a: The first number to add.
        b: The second number to add. Defaults to 98.

    Returns:
        int: The sum of ``a`` and ``b``.

    Raises:
        TypeError: If ``a`` or ``b`` is not an integer or a float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
