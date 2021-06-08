#!/usr/bin/python3
"""
Tests for Base class
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestBaseMethods(unittest.TestCase):
    """Testing Base class methods"""

    def test_id(self):
        """Problem 1. Tests IDs"""
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base()
        self.assertEqual(b3.id, 3)
        b4 = Base(12)
        self.assertEqual(b4.id, 12)
        b5 = Base()
        self.assertEqual(b5.id, 4)


if __name__ == '__main__':
    unittest.main()
