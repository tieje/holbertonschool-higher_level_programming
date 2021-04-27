#!/usr/bin/python3

def printAlphabet():
    for i in range(97, 123):
        if chr(i) == 'q':
            continue
        if chr(i) == 'e':
            continue
        print(chr(i), end="")
    return


printAlphabet()
