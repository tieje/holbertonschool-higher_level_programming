#!/usr/bin/python3
"""Base Geometry"""


class BaseGeometry:
    """Base Geometry"""

    def area(self):
        """Does nothing so far"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Integer validator"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
