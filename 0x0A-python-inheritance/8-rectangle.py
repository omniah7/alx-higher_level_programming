#!/usr/bin/python3

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """BaseGeometry class"""

    def __init__(self, width, height):
        """a constructor for rectangle"""
        __width = super().integer_validator('width', width)
        __height = super().integer_validator('height', height)
