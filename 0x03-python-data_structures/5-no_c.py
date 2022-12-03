#!/usr/bin/python3
def no_c(my_string):
    st = ""
    for char in my_string:
        st += char if char not in "cC" else ""
    return st
