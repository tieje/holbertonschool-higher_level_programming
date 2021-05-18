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
    Raises:
        ValueError: If the size isn't great than 0
        TypeError: If size is not an integer type
    """

    def __init__(self, size=0):
        if type(size) == int:
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """
        Returns:
            size squared
        """
        return self.__size ** 2
