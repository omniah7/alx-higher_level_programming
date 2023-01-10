#!/usr/bin/python3
"""pascal_triangle function"""


def pascal_triangle(n):
    """returns a list of lists of integers representing
    the Pascal`s triangle of n"""
    if n <= 0:
        return []
    list = [[1]]
    for r in range(1, n):
        row = [1]
        for c in range(1, r+1):
            # if last column
            if c == r:
                row += [1]
                break
            row += [list[r - 1][c] + list[r - 1][c - 1]]
        list += [row]
    return list
