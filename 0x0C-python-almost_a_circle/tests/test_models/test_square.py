#!/usr/bin/python3
"""
Tests for Square class
"""
import unittest
from models.square import Square


class TestSquareMethods(unittest.TestCase):
    """
    Square class tests
    """

    def test_string_input(self):
        '''String Input'''
        with self.assertRaises(TypeError):
            Square("word", 'up')

    def test_negative_size(self):
        '''Less than zero width, height input'''
        with self.assertRaises(ValueError):
            Square(-1)

    def test_zero_size(self):
        '''Zero width, height input'''
        with self.assertRaises(ValueError):
            Square(0)

    def test_negative_x_y(self):
        '''negative x and y'''
        with self.assertRaises(ValueError):
            Square(size=1, x=-1, y=-1)

    def test_Update_Args(self):
        """
        Problem 12, Square Update #0. Tests *args and **kwargs
        """
        # initialize
        s1 = Square(5, id=1)
        self.assertEqual(s1.__str__(), "[Square] (1) 0/0 - 5")
        # no arguments except id
        s1.update()
        self.assertEqual(s1.__str__(), "[Square] (1) 0/0 - 5")
        # one argument
        s1.update(10)
        self.assertEqual(s1.__str__(), "[Square] (10) 0/0 - 5")
        # two arguments
        s1.update(1, 2)
        self.assertEqual(s1.__str__(), "[Square] (1) 0/0 - 2")
        # three arguments
        s1.update(1, 2, 3)
        self.assertEqual(s1.__str__(), "[Square] (1) 3/0 - 2")
        # four arguments
        s1.update(1, 2, 3, 4)
        self.assertEqual(s1.__str__(), "[Square] (1) 3/4 - 2")
        # too many arguments
        s1.update(1, 2, 3, 4, 5, 6, 7)
        self.assertEqual(s1.__str__(), "[Square] (1) 3/4 - 2")
        # kwargs test all
        s1.update(size=7, id=89, y=1, x=12)
        self.assertEqual(s1.__str__(), "[Square] (89) 12/1 - 7")

    def test_Display(self):
        '''
        Problem 5 and 7. Display in terms of #s
        for square.
        '''
        s1 = Square(3, 2, 2)
        compare = "\n\n  ###  ###  ###"
        self.assertEqual(s1.display(), compare)

    def test_SaveToJson(self):
        """
        Problem 16, part 2: JSON string to file for Square
        """
        equal = [{"id": 3, "size": 10, "x": 7, "y": 2},
                 {"id": 4, "size": 2, "x": 4, "y": 0}]
        s1 = Square(10, 7, 2, id=3)
        s2 = Square(2, 4, id=4)
        Square.save_to_file([s1, s2])
        with open("Square.json", "r") as file:
            contents = file.read()
            self.assertEqual(eval(contents), equal)


if __name__ == '__main__':
    unittest.main()
