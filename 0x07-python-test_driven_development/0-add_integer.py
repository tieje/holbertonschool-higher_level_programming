#!/usr/bin/python3
"""
nothing on the outside
"""


def add_integer(a, b=98):
    """
    adds 2 integers
    Args
        a (int): integer
        b (int): integer default 98
    Returns:
        A single integer
    """
    if (type(a) != int and type(a) is not float)\
            or a is None:
        raise TypeError("a must be an integer")
    if type(b) != int and type(b) is not float:
        raise TypeError("b must be an integer")
    result = a + b
    if result == float('inf') or result == -float('inf'):
        raise TypeError("a must be an integer")
    return int(a) + int(b)
