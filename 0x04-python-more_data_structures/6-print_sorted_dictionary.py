#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sortkeys = sorted(a_dictionary.items())
    for key, value in sortkeys:
        print("{}: {}".format(key, value))
