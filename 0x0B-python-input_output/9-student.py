#!/usr/bin/python3
"""Student Module"""


class Student:
    """Student class"""

    def __init__(self, first_name, last_name, age):
        """define a student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves a dictionary representation of a
        Student instance (same as 8-class_to_json.py)"""
        return self.__dict__
