#!/usr/bin/python3
"""
Tests for Rectangle class
"""
import unittest
from models.rectangle import Rectangle
from models.base import Base
from unittest.mock import patch, call


class TestRectangleMethods(unittest.TestCase):
    """
    Tests for Rectangle class Methods
    """

    def test_Area(self):
        """
        Problem 4, Area First
        """
        # Minimum required inputs
        r1 = Rectangle(3, 2).area()
        self.assertEqual(r1, 6)
        # Maximum possible inputs
        r_max = Rectangle(8, 7, 1, 1, 12).area()
        self.assertEqual(r_max, 56)

    def test_Update_Args(self):
        """
        Problem 8, Update #0. Tests *args
        """
        # initialize
        r1 = Rectangle(10, 10, 10, 10, 1)
        self.assertEqual(r1.__str__(), "[Rectangle] (1) 10/10 - 10/10")
        # no arguments
        r1.update()
        self.assertEqual(r1.__str__(), "[Rectangle] (1) 10/10 - 10/10")
        # one argument
        r1.update(89)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 10/10 - 10/10")
        # two arguments
        r1.update(89, 2)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 10/10 - 2/10")
        # three arguments
        r1.update(89, 2, 3)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 10/10 - 2/3")
        # four arguments
        r1.update(89, 2, 3, 4)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 4/10 - 2/3")
        # five arguments
        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 4/5 - 2/3")
        # too many arguments
        r1.update(89, 2, 3, 4, 5, 6, 7, 8)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 4/5 - 2/3")

    def test_SaveToJson(self):
        """
        Problem 16, part 1: JSON string to file for Rectangle
        """
        equal = [{"x": 2, "y": 8, "id": 1, "height": 7, "width": 10},
                 {"x": 0, "y": 0, "id": 2, "height": 4, "width": 2}]
        r1 = Rectangle(10, 7, 2, 8, id=1)
        r2 = Rectangle(2, 4, id=2)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as file:
            contents = file.read()
            self.assertEqual(eval(contents), equal)

    def test_SaveToAndLoadFromCSV(self):
        """
        Problem 20, save to and read from CSV for
        both Rectangle and Square since they both rely
        on the same class method from Base class.
        """
        # Test normal operation
        r1 = Rectangle(10, 7, 2, 8, id=1)
        r2 = Rectangle(2, 4, id=2)
        list_rectangles_input = [r1, r2]
        Rectangle.save_to_file_csv(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file_csv()
        equal_1 = "[Rectangle] (1) 2/8 - 10/7"
        equal_2 = "[Rectangle] (2) 0/0 - 2/4"
        self.assertEqual(list_rectangles_output[0].__str__(), equal_1)
        self.assertEqual(list_rectangles_output[1].__str__(), equal_2)
        # Test empty list.
        Rectangle.save_to_file_csv([])
        list_rectangles_output = Rectangle.load_from_file_csv()
        self.assertEqual(list_rectangles_output, [])
        # Test non-existent file
        self.assertEqual(Base.load_from_file_csv(), [])


if __name__ == '__main__':
    unittest.main()
