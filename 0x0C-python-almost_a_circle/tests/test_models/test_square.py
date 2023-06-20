#!/usr/bin/python3
"""unittests for Rectangle Module"""
import unittest
from models.rectangle import Rectangle
from models.base import Base
from models.square import Square


class test_square(unittest.TestCase):
    """Test class for Square class"""
    def setUp(self):
        """instructions before each test method"""
        Base._Base__nb_objects = 0
