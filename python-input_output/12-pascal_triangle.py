#!/usr/bin/python3
"""Defines a Pascal's triangle function."""


def pascal_triangle(n):
    """Return a list of lists of integers representing Pascal's triangle.

    Args:
        n (int): The number of rows of the triangle.

    Returns:
        list: The rows of the triangle, or an empty list if ``n`` <= 0.
    """
    if n <= 0:
        return []

    triangle = [[1]]
    for row_number in range(1, n):
        previous = triangle[-1]
        row = [1]
        for i in range(len(previous) - 1):
            row.append(previous[i] + previous[i + 1])
        row.append(1)
        triangle.append(row)
    return triangle
