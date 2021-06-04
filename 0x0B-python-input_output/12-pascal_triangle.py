#!/usr/bin/python3
"""
Return a list of Integers representing Pascal's triangle of n
"""


def pascal_triangle(n):
    """
    Return a list of Integers representing Pascal's triangle of n
    """
    result = []
    if n > 0:
        for i in range(n):
            result.append(list(str(11**i)))
    return result
