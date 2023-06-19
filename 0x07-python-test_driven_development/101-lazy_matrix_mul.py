#!/usr/bin/python3
""" lazy_matrix_mul Function """
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """multiplies 2 matrices by using the module NumPy"""
    return np.matmul(m_a, m_b)
