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
    if type(a) == float:
        a = int(a)
    if type(b) == float:
        b = int(b)
    if type(a) != int:
        raise TypeError("a must be an integer")
    if type(b) == int:
        raise TypeError("b must be an integer")
    return a + b
