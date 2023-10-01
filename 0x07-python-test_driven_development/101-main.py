#!/usr/bin/python3

"""This module Defines a matrix multiplication function using NumPy."""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Return the multiplication of 2 matrix.

    Args:
        m_a (list of lists of ints and or floats): The first matrix.
        m_b (list of lists of ints and or floats): The second matrix.
    """

    return (np.matmul(m_a, m_b))
