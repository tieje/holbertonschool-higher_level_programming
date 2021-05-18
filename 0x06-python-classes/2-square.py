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
        """
        Initialize square.
        Args:
            size (int): A positive integer for the size of the square
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
