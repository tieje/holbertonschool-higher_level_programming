#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    Class for testing Max Integer function
    """
    def test_return_max(self):
        """
        tests basic usage
        """
        self.assertEqual(102, max_integer([1, 2, 100, 3, 102]))

    def test_return_none(self):
        """
        test return None when list is empty
        """
        self.assertEqual(None, max_integer([]))

    def test_default_none(self):
        """
        test return None when input is empty
        """
        self.assertEqual(None, max_integer())


if __name__ == '__main__':
    unittest.main()
