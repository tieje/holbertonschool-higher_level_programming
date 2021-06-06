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
        if args and args != () and args != None:
            ordered_list = ['id', 'size', 'x', 'y']
            for i in range(len(args)):
                # id is does not have _Rectangle__ prefix
                if i == 0:
                    self.__dict__[ordered_list[i]] = args[i]
                else:
                    self.__dict__['_Square__' + ordered_list[i]] = args[i]
        elif kwargs != None:
            for key, value in kwargs.items():
                if key == 'id':
                    self.__dict__[key] = value
                else:
                    self.__dict__[key] = value
    def to_dictionary(self):
        """returns dictionary of Rectangle"""
        """
        json_string = json.dumps(self.__dict__, default=lambda o: o.__dict__)
        replace_rectangle = json_string.replace('_Rectangle__', '').replace('_Square__', '')
        return json.loads(replace_rectangle)
        """
        return self.__dict__
