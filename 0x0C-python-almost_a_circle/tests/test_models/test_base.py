#!/usr/bin/python3
"""unittests for Base Module"""
import unittest
from models.base import Base


class test_base(unittest.TestCase):
    """Test class for Base class"""
    def setUp(self):
        """instructions before each test method"""
        Base.__nb_objects = 0

    def test_init(self):
        """test intialization if the object"""
        b = Base()
        self.assertEqual(b.id, 1)
        b = Base()
        self.assertEqual(b.id, 2)
        b = Base(56)
        self.assertEqual(b.id, 56)

    def test_to_json_string(self):
        """ test converting to a JSON representation """
        self.assertEqual(Base.to_json_string(None), '[]')
        self.assertEqual(Base.to_json_string([]), '[]')
        self.assertEqual(Base.to_json_string([{'id': 12}]), '[{"id": 12}]')

    def test_from_json_string(self):
        """test converting to a list of the JSON string representation"""
        self.assertEqual(Base.from_json_string("[]"), [])
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string('[{"id": 12}]'), [{"id": 12}])
