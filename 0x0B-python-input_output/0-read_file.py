#!/usr/bin/python3
"""This module reads a text file"""


def read_file(filename=""):
    """This method reads a file."""
    with open(filename, mode="r", encoding="utf_8") as file:
        for line in file:
            print(line, end='')
