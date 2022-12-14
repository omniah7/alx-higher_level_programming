#!/usr/bin/python3
"""Square module"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class"""

    def __init__(self, size):
        """define the square"""
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """area of the square"""
        return self.__size ** 2

    def __str__(self):
        """string representation"""
        return f"[Square] {self.__size}/{self.__size}"
