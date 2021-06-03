#!/usr/bin/python3
"""This module appends a string to a txt file"""


def append_write(filename="", text=""):
    """Append a string a txt file"""
    with open(filename, mode='a', encoding='utf_8') as file:
        file.write(text)
    return len(text)
