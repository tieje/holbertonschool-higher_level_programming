#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    arglen = len(argv)
    arguments = "arguments"
    suffix = ":"
    if arglen == 1:
        suffix = "."
    if arglen == 2:
        arguments = "argument"
    print("{} {}{}".format(arglen - 1, arguments, suffix))
    if arglen > 1:
        for i in range(1, arglen):
            print("{}: {}".format(i, argv[i]))
