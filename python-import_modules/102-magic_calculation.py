#!/usr/bin/python3
"""Defines magic_calculation, reconstructed from bytecode."""


def magic_calculation(a, b):
    """Perform a magic calculation.

    Args:
        a: first integer
        b: second integer

    Returns:
        The result of the calculation.
    """
    from magic_calculation_102 import add, sub

    if a < b:
        c = add(a, b)

        for i in range(4, 6):
            c = add(c, i)

        return c

    else:
        return sub(a, b)
