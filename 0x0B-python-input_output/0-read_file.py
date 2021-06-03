#!/usr/bin/python3
"""This module reads a text file"""


def read_file(filename=""):
    """This method reads a file."""
    with open(filename, mode="r", encoding="UTF8") as file:
        print(file.read())
        file.close()
