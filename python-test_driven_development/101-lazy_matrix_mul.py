#!/usr/bin/python3
"""Defines a lazy matrix multiplication function.

This module exposes a single function, ``lazy_matrix_mul``, which computes
the matrix product of two matrices using the NumPy module.
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Return the matrix product of ``m_a`` and ``m_b`` using NumPy.

    Args:
        m_a (list): The first matrix, a list of lists of int/float.
        m_b (list): The second matrix, a list of lists of int/float.

    Returns:
        numpy.ndarray: The product of ``m_a`` and ``m_b``.
    """
    return np.matmul(m_a, m_b)
