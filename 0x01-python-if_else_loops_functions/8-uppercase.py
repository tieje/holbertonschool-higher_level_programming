#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(i) < 124 and ord(i) > 96:
            print("{}".format(chr(ord(i) - 32)), end="")
        else:
            print("{}".format(i), end="")
    print("")
    return



uppercase("a string")
uppercase("ThisstING")
uppercase("98 Battery Street")
