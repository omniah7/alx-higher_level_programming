#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        n = 0
        for e in range(x):
            print(my_list[e], end="")
            n += 1
        print()
        return n
    except IndexError:
        print()
        return n
