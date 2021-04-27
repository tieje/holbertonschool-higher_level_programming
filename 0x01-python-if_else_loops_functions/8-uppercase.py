#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        ordOf = ord(str[i])
        if ordOf < 92 and ordOf > 64:
            printThis = str[i]
        elif ordOf < 124 and ordOf > 96:
            printThis = chr(ordOf - 32)
        print(printThis, end="")
    print("")
    return

"""
uppercase("a string")
uppercase("ThisstING")
"""