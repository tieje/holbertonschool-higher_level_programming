#!/usr/bin/python3
"""
nothing outside functions
"""


def text_indentation(text):
    """
    prints a text with 2 new lines after each of ".", "?", and ":"
    text (string)
    """
    if type(text) != str:
        raise TypeError("text must be a string")
    text_list = text.replace('.', '.splithere').replace(
        '?', '?splithere').replace(':', ':splithere').split('splithere')
    for i in range(len(text_list) - 1):
        print(text_list[i].strip() + "\n")
    print(text_list[-1].strip(), end="")
