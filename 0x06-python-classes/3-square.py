#!/usr/bin/python3
"""a class Square that defines a square by: (based on 2-square.py)"""


class Square:
    def __init__(self, size=0):
        """defines a square
            Args:
                size (int): The size of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    
    def area(self):
        """the square area
        Return:
            area of the square
        """
        return self.__size**2
