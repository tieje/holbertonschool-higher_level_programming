#!/usr/bin/python3
def uppercase(str):
    for i in str:
        a = i
        if ord(i) < 124 and ord(i) > 96:
            a = chr(ord(i) - 32)
        print("{}".format(a), end="")
    print("")
    return


"""
uppercase("a string")
uppercase("ThisstING")
uppercase("98 Battery Street")
"""
