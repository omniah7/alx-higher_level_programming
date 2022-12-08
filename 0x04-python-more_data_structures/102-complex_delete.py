#!/usr/bin/python3
def complex_delete(dict, value):
    for k, v in tuple(dict.items()):
        if v == value:
            del dict[k]
    return dict
