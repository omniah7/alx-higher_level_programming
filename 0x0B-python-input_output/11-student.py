#!/usr/bin/python3
"""Student Module"""


class Student:
    """Student class"""

    def __init__(self, first_name, last_name, age):
        """define a student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a
        Student instance (same as 8-class_to_json.py)"""
        if (type(attrs) == list and
                all(type(i) == str for i in attrs)):
            return {key: getattr(self, key) for key in attrs
                    if hasattr(self, key)}
        return self.__dict__

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance"""
        for key, value in json.items():
            setattr(self, key, value)
