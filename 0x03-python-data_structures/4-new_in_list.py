#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    copy = my_list.copy()  # or my_list[:]
    # if not (negative) or (out of range)
    if (idx >= 0) and (idx < len(my_list)):
        copy[idx] = element
    return copy
