#!/usr/bin/python3
"""unittests for Rectangle Module"""
import unittest
from models.rectangle import Rectangle
from models.base import Base
from io import StringIO
import sys


class test_base(unittest.TestCase):
    """Test class for Rectangle class"""
    def setUp(self):
        """instructions before each test method"""
        Base._Base__nb_objects = 0

    def test_init(self):
        """test intialization if the object"""
        # r = Rectangle(4, 2)
        # self.assertEqual(r.height, 2)
        # self.assertEqual(r.width, 4)

        # r = Rectangle(4, 2, 1, 3)
        # self.assertEqual(r.x, 1)
        # self.assertEqual(r.y, 3)

        r = Rectangle(1, 2)
        self.assertEqual(r.id, 1)
        r = Rectangle(2, 3)
        self.assertEqual(r.id, 2)
        r = Rectangle(3, 4)
        self.assertEqual(r.id, 3)
        r = Rectangle(10, 2, 4, 5, -5)
        self.assertEqual(r.id, -5)

        r = Rectangle(4, 2, 1, 3, 76)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.width, 4)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 3)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.id, 76)

        with self.assertRaises(TypeError) as x:
            r = Rectangle('4', 2, 1, 3)
            self.assertEqual(
                'width must be an integer', str(x.exception)
                )
        with self.assertRaises(TypeError) as x:
            r = Rectangle(4, '2', 1, 3)
            self.assertEqual(
                'height must be an integer', str(x.exception)
                )
        with self.assertRaises(TypeError) as x:
            r = Rectangle(4, 2, '1', 3)
            self.assertEqual(
                'x must be an integer', str(x.exception)
                )
        with self.assertRaises(TypeError) as x:
            r = Rectangle(4, 2, 1, '3')
            self.assertEqual(
                'y must be an integer', str(x.exception)
                )
        with self.assertRaises(ValueError) as x:
            r = Rectangle(-4, 2)
            self.assertEqual(
                'width must be > 0', str(x.exception)
                )
        with self.assertRaises(ValueError) as x:
            r = Rectangle(0, 2)
            self.assertEqual(
                'width must be > 0', str(x.exception)
                )
        with self.assertRaises(ValueError) as x:
            r = Rectangle(4, -2)
            self.assertEqual(
                'height must be > 0', str(x.exception)
                )
        with self.assertRaises(ValueError) as x:
            r = Rectangle(4, 0)
            self.assertEqual(
                'height must be > 0', str(x.exception)
                )
        with self.assertRaises(ValueError) as x:
            r = Rectangle(4, 2, -1, 1)
            self.assertEqual(
                'x must be >= 0', str(x.exception)
                )
        with self.assertRaises(ValueError) as x:
            r = Rectangle(4, 2, 1, -1)
            self.assertEqual(
                'y must be >= 0', str(x.exception)
                )

    def test_area(self):
        """test the area function"""
        r = Rectangle(3, 2)
        self.assertEqual(r.area(), 6)
        r = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r.area(), 56)

    def test_display(self):
        """test the display function"""
        sys.stdout = s = StringIO()

        r = Rectangle(4, 6)
        r.display()
        self.assertEqual(
            s.getvalue(), "####\n####\n####\n####\n####\n####\n")

        s.truncate(0)  # clear the variable 's'
        s.seek(0)
        r = Rectangle(2, 3, 2, 2)
        r.display()
        self.assertEqual(
            s.getvalue(), "\n\n  ##\n  ##\n  ##\n")

        s.truncate(0)  # clear the variable 's'
        s.seek(0)
        r = Rectangle(2, 3, 2)
        r.display()
        self.assertEqual(
            s.getvalue(), "  ##\n  ##\n  ##\n")
        sys.stdout = sys.__stdout__  # Reset redirect.

    def test__str__(self):
        """test the str representaion"""
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r), '[Rectangle] (12) 2/1 - 4/6')
        self.assertEqual(Rectangle.__nb_objects, 0)
        r = Rectangle(5, 5, 1)
        self.assertEqual(str(r), '[Rectangle] (1) 1/0 - 5/5')

    def test_update(self):
        """test update function"""
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89)
        self.assertEqual(r1.id, 89)
        r1.update(89, 2)
        self.assertEqual(r1.width, 2)
        r1.update(89, 2, 3)
        self.assertEqual(r1.height, 3)
        r1.update(89, 2, 3, 4)
        self.assertEqual(r1.x, 4)
        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(r1.y, 5)

        r1 = Rectangle(10, 10, 10, 10)
        r1.update(height=1)
        self.assertEqual(r1.height, 1)
        r1.update(width=1, x=2)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.x, 2)
        r1.update(y=1, width=2, x=3, id=89)
        self.assertEqual(r1.y, 1)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.id, 89)
        r1.update(**{'x': 1, 'height': 2, 'y': 3, 'width': 4})
        self.assertEqual(r1.x, 1)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.y, 3)
        self.assertEqual(r1.width, 4)

    def test_to_dictionary(self):
        """test converting into a dictionary"""
        pass

    def test_create(self):
        """test cresting dictionaries"""
        # r = Rectangle.create(**{ 'id': 89 })

        # r = Rectangle.create(**{ 'id': 89, 'width': 1 })

        # r = Rectangle.create(**{ 'id': 89, 'width': 1, 'height': 2 })

        # Rectangle.create(**{ 'id': 89, 'width': 1, 'height': 2, 'x': 3 })

        r = Rectangle.create(
            **{'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4})
        self.assertEqual(r.x, 3)
        self.assertEqual(r.id, 89)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.y, 4)
        self.assertEqual(r.width, 1)
