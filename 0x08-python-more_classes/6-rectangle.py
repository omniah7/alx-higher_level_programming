#!/usr/bin/python3
"""Ractangle module"""


class Rectangle:
    """Rectangle class"""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """defines a rectangle
        Args:
            width(int): rectangle width.
            height(int): rectangle height.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """a getter for width attribute"""
        return self.__width

    @property
    def height(self):
        """a getter for height attribute"""
        return self.__height

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns the rectangle area"""
        return self.width * self.height

    def perimeter(self):
        """returns the rectangle perimeter"""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """a string format for the object"""
        if self.width == 0 or self.height == 0:
            return ""
        row = '#' * self.width
        s = row
        s += ("\n"+row) * (self.height - 1)
        return s

    def __repr__(self):
        """returns a string representation of the rectangle
        to be able to recreate a new instance by using eval()
        """
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """Print the message 'Bye rectangle...'
        when an instance of Rectangle is deleted
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
