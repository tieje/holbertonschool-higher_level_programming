#!/usr/bin/python3
def raise_exception():
    try:
        res = 1 / 0
    except:
        raise Exception("Exception raised")
