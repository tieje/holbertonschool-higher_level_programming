#!/usr/bin/python3
"""
Defining a rectangle
"""


class Rectangle:
    """
    class that will define a rectangle
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Create a rectangle"""
        self.width = width
        self.height = height
        __class__.number_of_instances += 1

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
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the perimeter of the rectangle"""
        if self.__width == 0 or\
                self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """returns the string rectangle with #"""
        if self.__width == 0 or\
                self.__height == 0:
            return ''
        final = []
        for i in range(self.__height):
            final.append(str(self.print_symbol) * self.__width)
        return '\n'.join(final)

    def __repr__(self):
        """returns the repr rectange with #"""
        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    def __del__(self):
        """prints deletion statement"""
        print("Bye rectangle...")
        __class__.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns bigger or equal"""
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_2.area() > rect_1.area():
            return rect_2
        return rect_1

    @classmethod
    def square(cls, size=0):
        return Rectangle(size, size)
