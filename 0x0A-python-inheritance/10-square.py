#!/usr/bin/python3
"""Square module"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class"""

    def __init__(self, size):
        """define the square"""
        super().super().integer_validator('size', size)
        self.__size = size

    def area(self):
        """area of the square"""
        return self.__size**2
