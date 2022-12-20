#!/usr/bin/python3
"""
    a class Square that defines a square by: (based on 0-square.py)
    attributes:
        Private instance attribute: size
        Instantiation with size (no type/value verification)
"""


class Square:
    def __init__(self, n):
        self.__size = n
