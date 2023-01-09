#!/usr/bin/python3

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """BaseGeometry class"""

    def __init__(self, width, height):
        """a constructor for rectangle"""
        super().integer_validator('width', width)
        self.__width = width
        super().integer_validator('height', height)
        self.__height = height

    def __str__(self):
        """string representation"""
        return f"[Rectangle] {self.__width}/{self.__height}"

    def area(self):
        """the area of the rectangle"""
        return self.__width * self.__height
