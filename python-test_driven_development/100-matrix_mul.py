#!/usr/bin/python3
"""Defines a matrix multiplication function.

This module exposes a single function, ``matrix_mul``, which computes the
matrix product of two matrices without using any external module.
"""


def matrix_mul(m_a, m_b):
    """Return the matrix product of ``m_a`` and ``m_b``.

    Args:
        m_a (list): The first matrix, a list of lists of int/float.
        m_b (list): The second matrix, a list of lists of int/float.

    Returns:
        list: A new matrix holding the product of ``m_a`` and ``m_b``.

    Raises:
        TypeError: If ``m_a`` or ``m_b`` is not a list.
        TypeError: If ``m_a`` or ``m_b`` is not a list of lists.
        ValueError: If ``m_a`` or ``m_b`` is empty.
        TypeError: If ``m_a`` or ``m_b`` contains a non int/float element.
        TypeError: If the rows of ``m_a`` or ``m_b`` differ in size.
        ValueError: If ``m_a`` and ``m_b`` cannot be multiplied.
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    for row in m_a:
        if not isinstance(row, list):
            raise TypeError("m_a must be a list of lists")
    for row in m_b:
        if not isinstance(row, list):
            raise TypeError("m_b must be a list of lists")

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    for row in m_a:
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("m_a should contain only integers or floats")
    for row in m_b:
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("m_b should contain only integers or floats")

    for row in m_a:
        if len(row) != len(m_a[0]):
            raise TypeError("each row of m_a must be of the same size")
    for row in m_b:
        if len(row) != len(m_b[0]):
            raise TypeError("each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    result = []
    for i in range(len(m_a)):
        new_row = []
        for j in range(len(m_b[0])):
            total = 0
            for k in range(len(m_b)):
                total += m_a[i][k] * m_b[k][j]
            new_row.append(total)
        result.append(new_row)
    return result
