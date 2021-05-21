#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_return_max(self):
        self.assertEqual(102, max_integer([1, 2, 100, 3, 102]))

    def test_return_none(self):
        self.assertEqual(None, max_integer([]))

    def test_default_none(self):
        self.assertEqual(None, max_integer())


if __name__ == '__main__':
    unittest.main()
