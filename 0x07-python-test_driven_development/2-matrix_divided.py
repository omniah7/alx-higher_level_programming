#!/usr/bin/python3
""" matrix_divided Function """


def matrix_divided(matrix, div):
    """divides all elements of a matrix
    Args:
        matrix (list of lists): The matrix
        div (int): The dividing number
    Raises:
        TypeError: if matrix is not a list of lists of int or float.
        TypeError: if each row of matrix is not of same size.
        TypeError: if div is neither an int nor float
        ZeroDivisionError: if div is zero
    Returns:
        a new matrix with elements rounded to 2 decimal places.
    """
    if not (isinstance(matrix, list)
            and all(isinstance(l, list) for l in matrix)
            and all(isinstance(i, int) or isinstance(i, float)
            for l in matrix for i in l)):
        raise TypeError(
            'matrix must be a matrix (list of lists) of integers/floats'
            )

    if not len(set(map(len, matrix))) == 1:
        raise TypeError('Each row of the matrix must have the same size')

    if not (isinstance(div, int) or isinstance(div, float)):
        raise TypeError('div must be a number')

    if div == 0:
        raise ZeroDivisionError('division by zero')

    new = [[round(x/div, 2) for x in r] for r in matrix]
    return new
