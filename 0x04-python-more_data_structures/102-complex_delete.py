#!/usr/bin/python3
def complex_delete(dict, value):
    new_dict = dict.copy()
    for k, v in dict.items():
        if v is value:
            del new_dict[k]
    return new_dict
