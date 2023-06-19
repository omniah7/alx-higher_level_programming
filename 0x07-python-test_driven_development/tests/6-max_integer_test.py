#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """ unittests for the function 'max_integer' """

    def test_max_integer(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 2, 10, 4]), 10)
        self.assertEqual(max_integer([-1, -3, -2, -4]), -1)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([0]), 0)
