#!/usr/bin/python3
"""
Class that defines a student
"""


class Student:
    """
    Class that defines a student
    """

    def __init__(self, first_name, last_name, age):
        """Initialize the student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Returns dictionary representation of self
        """
        def check_string(x): return type(x) is str
        if type(attrs) is list and all(list(map(check_string, attrs))):
            return {i: j for i, j in self.__dict__.items() if i in attrs}
        return self.__dict__
