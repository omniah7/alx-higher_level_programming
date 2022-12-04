#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if (idx < 0) or (idx >= len(my_list)):  # if (negative) or (out of range)
        return my_list
    del my_list[idx]  # delete from my_list
    return my_list
