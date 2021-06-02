#!/usr/bin/python3
""" example class"""


class MyList(list):
    """This class extends list class"""
    def print_sorted(self):
        """Print a sorted list"""
        print(sorted(self))
