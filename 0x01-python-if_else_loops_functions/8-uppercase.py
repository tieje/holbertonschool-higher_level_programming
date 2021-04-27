#!/usr/bin/python3
def uppercase(str):
    printThis = ""
    newline = "\n"
    for i in str:
        ordOf = ord(i)
        printThis = i
        if ordOf < 124 and ordOf > 96:
            printThis = chr(ordOf - 32)
        print("{}".format(printThis), end="")
    print("{}".format(newline))
    return


"""
uppercase("a string")
uppercase("ThisstING")
uppercase("98 Battery Street")
"""