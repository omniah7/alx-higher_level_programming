#!/usr/bin/python3
"""Square module"""

class Square:
    """Square class"""

    def __init__(self, size=0):
        """defines a square
            Args:
                size (int): The size of the square
        """
        self.__size = size

    @property
    def size(self):
        """ getter for property size"""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """the square area
            Return:
                area of the square
        """
        return self.__size**2
