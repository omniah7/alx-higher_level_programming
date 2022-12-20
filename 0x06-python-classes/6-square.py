#!/usr/bin/python3
"""Square module"""


class Square:
    """Square class"""

    def __init__(self, size=0, position=(0, 0)):
        """defines a square
            Args:
                size (int): The size of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

        if not isinstance(position, (int, int)) or position[0] < 0 \
                or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

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

    @property
    def position(self):
        """getter for property position"""
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, (int, int)) or value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """the square area
            Return:
                area of the square
        """
        return self.__size**2

    def my_print(self):
        """prints in stdout the square with the character #"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for j in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)
