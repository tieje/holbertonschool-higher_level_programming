#!/usr/bin/python3
"""
Rectangle code
"""
from models.base import Base


class Rectangle(Base):
    """
    Rectangle code
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for width"""
        var_name = 'width'
        Rectangle.check_int(value, var_name)
        Rectangle.check_width_height(value, var_name)
        self.__width = value

    @property
    def height(self):
        """getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for height"""
        var_name = 'height'
        Rectangle.check_int(value, var_name)
        Rectangle.check_width_height(value, var_name)
        self.__height = value

    @property
    def x(self):
        """getter for x"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter for x"""
        var_name = 'height'
        Rectangle.check_int(value, var_name)
        Rectangle.check_x_y(value, var_name)
        self.__x = value

    @property
    def y(self):
        """getter for y"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter for y"""
        var_name = 'height'
        Rectangle.check_int(value, var_name)
        Rectangle.check_x_y(value, var_name)
        self.__y = value

    @staticmethod
    def check_int(x, name):
        """if input is not an integer raise error"""
        if type(x) is not int:
            raise TypeError('{} must be an integer'.format(name))

    @staticmethod
    def check_width_height(x, name):
        """if width or height is not greater than 0 raise error"""
        if x <= 0:
            raise ValueError('{} must be > 0'.format(name))

    @staticmethod
    def check_x_y(x, name):
        """if x or y is not is less than 0 raise error"""
        if x < 0:
            raise ValueError('{} must be >= 0'.format(name))

    def area(self):
        """returns the area of the rectangle"""
        return self.width * self.height

    def display(self):
        """prints the rectangle in character #"""
        for i in range(self.y):
            print()
        for i in range(self.height):
            print(' ' * self.x + '#' * self.width)

    def __str__(self):
        """returns shape and width/height"""
        return "[{}] ({}) {}/{} - {}/{}".format(
            __class__.__name__,
            self.id, self.x, self.y, self.width, self.height)
    def update(self, *args):
        """assigns an argument to each attribute"""
        ordered_list = ['id', 'width', 'height', 'x', 'y']
        for i in range(len(args)):
            # id is does not have _Rectangle__ prefix
            if i == 0:
                self.__dict__[ordered_list[i]] = args[i]
            else:
                self.__dict__['_Rectangle__' + ordered_list[i]] = args[i]
