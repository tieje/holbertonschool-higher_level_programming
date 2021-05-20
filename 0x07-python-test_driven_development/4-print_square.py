#!/usr/bin/python3
"""
nothing outside functions
"""


def print_square(size):
    """
    prints a square with the #
    Args:
        size (int)
    """
    # size tests
    a = "size must be an integer"
    if type(size) == float and size < 0:
        raise TypeError(a)
    if type(size) != int or (type(size) == float and size < 0):
        raise TypeError(a)
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)
