#!/usr/bin/python3
"""
No module-level stuff here.
"""


class Square:
    """
    This class is all about squares.
    Args:
        size (int): size of the square
    Attributes:
        __size (int): size of the square
    """

    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def position(self):
        """
        tuple: two positive integers
        """
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) != tuple or len(value) != 2 or type(value[0]) != int or type(value[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    @property
    def size(self):
        """
        int: the getter for size
        """
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Returns:
            int: size squared
        Raises:
            ValueError: If the size isn't great than 0
            TypeError: If size is not an integer type
        """
        return self.__size ** 2

    def my_print(self):
        """
        print the square with character, #
        Returns:
            void: nothing
        """
        if self.__size == 0:
            print("")
            return
        for i in range(self.__size):
            for y in range(self.__position[0]):
                if y < self.__position[0]:
                    print(" ", end="")
            for x in range(self.__size):
                print("#", end="")
            print("")
        if self.__position[1] < 1:
            print("")
        return
