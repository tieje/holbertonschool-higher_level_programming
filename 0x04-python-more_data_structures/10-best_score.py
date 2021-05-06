#!/usr/bin/python3
def best_score(a_dictionary):
    maxkey = None
    if a_dictionary:
        maxkey = max(a_dictionary, key=a_dictionary.get)
    return maxkey
