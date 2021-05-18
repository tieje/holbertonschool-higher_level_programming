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

    def __init__(self, size=0):
        self.__size = size

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
            for x in range(self.__size):
                print("#", end="")
            print("")
        return
