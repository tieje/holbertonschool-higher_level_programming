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


class Rectangle(BaseGeometry):
    """Base Rectangle"""

    def __init__(self, width, height):
        """Initialize a Rectangle"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Overwrites old area method"""
        return self.__width * self.__height

    def __str__(self):
        """Returns string"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)


class Square(Rectangle):
    """Create a Square"""

    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)

