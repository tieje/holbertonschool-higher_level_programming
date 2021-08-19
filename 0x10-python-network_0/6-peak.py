#!/usr/bin/python3
'''find peak function only'''


def find_peak(list_of_integers):
    '''finds the greatest number from the list'''
    if list_of_integers:
        list_of_integers.sort()
        return(list_of_integers[-1])
    return None
