#!/usr/bin/python3
"""add_attribute function"""


def add_attribute(self, attr, value):
    """adds a new attribute to an object if it is possible"""
    if not hasattr(self, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(self, attr, value)
