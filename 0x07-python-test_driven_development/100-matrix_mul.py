#!/usr/bin/python3
""" matrix_mul Function"""


def matrix_mul(m_a, m_b):
    """multiplies 2 matrices"""
    if type(m_a) is not list:
        raise TypeError('m_a must be a list')
    if type(m_b) is not list:
        raise TypeError('m_b must be a list')

    if not all(type(ls) is list for ls in m_a):
        raise TypeError('m_a must be a list of lists')
    if not all(type(ls) is list for ls in m_b):
        raise TypeError('m_b must be a list of lists')

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    if not all(type(e) is int or type(e) is float for r in m_a for e in r):
        raise TypeError('m_a should contain only integers or floats')
    if not all(type(e) is int or type(e) is float for r in m_b for e in r):
        raise TypeError('m_b should contain only integers or floats')

    if len(set(map(len, m_a))) != 1:
        raise TypeError('each row of m_a must be of the same size')
    if len(set(map(len, m_b))) != 1:
        raise TypeError('each row of m_b must be of the same size')

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    new = []
    for i in range(len(m_a)):  # A row index
        new.append([])
        for j in range(len(m_b[0])):  # B col index
            sum = 0
            for n in range(len(m_a[0])):  # A col index
                sum += m_a[i][n]*m_b[n][j]
            new[i].append(sum)
    return new
