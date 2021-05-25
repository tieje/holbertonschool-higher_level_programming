#!/usr/bin/python3
"""
defining a rectangle
"""


class Rectangle:
    """
    class that will define a rectangle
    """

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    @property
    def height(self):
        """
        returns height property
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        sets the height value
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise TypeError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """
        returns property of width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        sets the width
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
