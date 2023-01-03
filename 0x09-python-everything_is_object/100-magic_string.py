#!/usr/bin/python3
def magic_string():
    magic_string.attribute = getattr(magic_string, "attribute", 0) + 1
    return 'BestSchool, ' * (magic_string.attribute - 1) + 'BestSchool'
