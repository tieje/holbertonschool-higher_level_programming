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
    def check_int(attr, name):
        """if input is not an integer raise error"""
        if type(attr) is not int:
            raise TypeError('{} must be an integer'.format(name))

    @staticmethod
    def check_width_height(attr, name):
        """if width or height is not greater than 0 raise error"""
        if attr <= 0:
            raise ValueError('{} must be > 0'.format(name))

    @staticmethod
    def check_x_y(attr, name):
        """if x or y is not is less than 0 raise error"""
        if attr < 0:
            raise ValueError('{} must be >= 0'.format(name))

    def area(self):
        """returns the area of the rectangle"""
        return self.width * self.height

    def display(self):
        """prints the rectangle in character #"""
        test_display = []
        for i in range(self.y):
            print()
            test_display.append('\n')
        for i in range(self.height):
            print_this = ' ' * self.x + '#' * self.width
            print(print_this)
            test_display.append(print_this)
        return ''.join(test_display)

    def __str__(self):
        """returns shape and width/height"""
        return "[{}] ({}) {}/{} - {}/{}".format(
            __class__.__name__,
            self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""
        if args and args != () and args != None:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[i]
                elif i == 1:
                    self.__width = args[i]
                elif i == 2:
                    self.__height = args[i]
                elif i == 3:
                    self.__x = args[i]
                elif i == 4:
                    self.__y = args[i]
        elif kwargs != None:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                elif key == 'width':
                    self.__width = value
                elif key == 'height':
                    self.__height = value
                elif key == 'x':
                    self.__x = value
                elif key == 'y':
                    self.__y = value

    def to_dictionary(self):
        """returns dictionary of Rectangle"""
        dictionary = {'x': self.__x, 'y': self.__y, 'id': self.id,
                      'height': self.__height, 'width': self.__width}
        return dictionary
