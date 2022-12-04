#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    len_a = len(tuple_a)
    len_b = len(tuple_b)
    a = list(tuple_a)
    b = list(tuple_b)
    if len_a < 2:
        for i in range(len_a - 1, 2):
            a.append(0)
    if len_b < 2:
        for i in range(len_b - 1, 2):
            b.append(0)
    sum_tuple = (a[0] + b[0], a[1] + b[1])
    return sum_tuple
    


