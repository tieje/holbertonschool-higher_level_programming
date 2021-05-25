#!/usr/bin/python3
"""
Defining a rectangle
"""


class Rectangle:
    """
    class that will define a rectangle
    """

    def __init__(self, width=0, height=0):
        """Create a rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Returns property of width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Returns height property
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height value
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise TypeError("height must be >= 0")
        self.__height = value
