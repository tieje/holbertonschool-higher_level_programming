#!/usr/bin/python3
"""Module is not special yet"""


def inherits_from(obj, a_class):
    """returns True is object is a sub class of the class"""
    if isinstance(obj, a_class) and type(obj) != a_class:
        return True
    return False
