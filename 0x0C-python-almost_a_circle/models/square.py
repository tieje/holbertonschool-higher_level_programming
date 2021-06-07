#!/usr/bin/python3
"""
A Square Boi
"""
from models.rectangle import Rectangle
import json


class Square(Rectangle):
    """
    Classy Square
    """

    def __init__(self, size, x=0, y=0, id=None):
        self.size = size
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """return private size"""
        return self.__size

    @size.setter
    def size(self, value):
        """set size to new value"""
        var_name = 'size'
        Rectangle.check_int(value, var_name)
        Rectangle.check_width_height(value, var_name)
        self.__size = value

    @property
    def x(self):
        """return private x"""
        return self.__x

    @x.setter
    def x(self, value):
        """set private x for square"""
        var_name = 'x'
        Rectangle.check_int(value, var_name)
        Rectangle.check_x_y(value, var_name)
        self.__x = value

    @property
    def y(self):
        """return private x"""
        return self.__y

    @y.setter
    def y(self, value):
        """set private x for square"""
        var_name = 'y'
        Rectangle.check_int(value, var_name)
        Rectangle.check_x_y(value, var_name)
        self.__y = value

    def __str__(self):
        """square details"""
        return "[{}] ({}) {}/{} - {}".format(
            __class__.__name__,
            self.id, self.x, self.y, self.size)

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""
        if args and args != () and args != None:
            for i in range(len(args)):
                # id is does not have _Rectangle__ prefix
                if i == 0:
                    self.id = args[i]
                elif i == 1:
                    self.__size = args[i]
                elif i == 2:
                    self.__x = args[i]
                elif i == 3:
                    self.__y = args[i]
        elif kwargs != None:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                elif key == 'size':
                    self.__size = value
                elif key == 'x':
                    self.__x = value
                elif key == 'y':
                    self.__y = value

    def to_dictionary(self):
        """returns dictionary of Square"""
        dictionary = {'id': self.id, 'size': self.__size,
                      'x': self.__x, 'y': self.__y}
        return dictionary
