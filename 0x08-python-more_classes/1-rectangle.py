#!/usr/bin/python3
"""
defining a rectangle
"""


class Rectangle:
    """
    class that will define a rectangle
    """

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        returns property of width
        """
        return self.width

    @width.setter
    def width(self, value):
        """
        sets the width
        """
        pass

    @property
    def height(self):
        """
        returns height property
        """
        return self.height
    
    @height.setter
    def height(self):
        """
        sets the height value
        """
        pass
