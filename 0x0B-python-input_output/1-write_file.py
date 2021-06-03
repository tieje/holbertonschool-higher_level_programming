#!/usr/bin/python3
"""This module writes a string to a txt file"""


def write_file(filename="", text=""):
    """Write a string a txt file"""
    with open(filename, mode='w', encoding='utf_8') as file:
        file.write(text)
    return len(text)
