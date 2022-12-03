#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix == [[]]:
        print()
        return
    for row in matrix:
        last = len(row) - 1  # last element in row
        for i in range(0, last):
            print("{:d}".format(row[i]), end=' ')
        print("{:d}".format(row[last]))  # print last element and '\n'
