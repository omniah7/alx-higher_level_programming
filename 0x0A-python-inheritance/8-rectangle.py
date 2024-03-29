#!/usr/bin/python3
"""Rectangle module"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """BaseGeometry class"""

    def __init__(self, width, height):
        """a constructor for rectangle"""
        super().integer_validator('width', width)
        super().integer_validator('height', height)
