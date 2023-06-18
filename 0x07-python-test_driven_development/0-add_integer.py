#!/usr/bin/python3
""" add_integer Function """


def add_integer(a, b=98):
    """ a function that adds 2 integers
    Args:
        a (int): integer value
        b (int): integer value if specified, otherwise 98
    Returns:
        sum of two integers
    Raises:
        TypeError: if either a or b are not integers
    """
    if not (isinstance(a, int) or isinstance(a, float)):
        raise TypeError('a must be an integer')
    if not (isinstance(b, int) or isinstance(b, float)):
        raise TypeError('b must be an integer')
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return a + b
