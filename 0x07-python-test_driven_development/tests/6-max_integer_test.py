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

    def test_max_at_beginning(self):
        """
        test for max value at the beginning of list
        """
        self.assertEqual(100, max_integer([100, 1, 3, 4]))

    def test_max_in_middle(self):
        """
        test for max value in the middle of the list
        """
        self.assertEqual(100, max_integer([1, 2, 100, 4, 5]))

    def test_negative(self):
        """
        test for negative number in list
        """
        self.assertEqual(100, max_integer([1, 2, -100, 100, -3, -5]))

    def test_only_negatives(self):
        """
        test for negative number in list
        """
        self.assertEqual(-1, max_integer([-1, -2, -100, -3, -5]))

    def test_for_one_element(self):
        """
        test for only one element
        """
        self.assertEqual(1, max_integer([1]))


if __name__ == '__main__':
    unittest.main()
