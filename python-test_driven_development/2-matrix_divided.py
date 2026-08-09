#!/usr/bin/python3
"""Defines a matrix division function.

This module exposes a single function, ``matrix_divided``, which divides
every element of a matrix by a given number.
"""


def matrix_divided(matrix, div):
    """Divide all elements of ``matrix`` by ``div``.

    Args:
        matrix (list): A list of lists of integers or floats.
        div (int/float): The divisor.

    Returns:
        list: A new matrix with every element divided by ``div`` and
        rounded to 2 decimal places.

    Raises:
        TypeError: If ``matrix`` is not a list of lists of int/float.
        TypeError: If the rows of ``matrix`` are not all the same size.
        TypeError: If ``div`` is not an integer or a float.
        ZeroDivisionError: If ``div`` is 0.
    """
    err = "matrix must be a matrix (list of lists) of integers/floats"

    if not isinstance(matrix, list) or matrix == []:
        raise TypeError(err)
    for row in matrix:
        if not isinstance(row, list) or row == []:
            raise TypeError(err)
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError(err)

    size = len(matrix[0])
    for row in matrix:
        if len(row) != size:
            raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(element / div, 2) for element in row] for row in matrix]
