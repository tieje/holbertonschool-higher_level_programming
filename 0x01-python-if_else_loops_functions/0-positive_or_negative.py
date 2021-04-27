#!/usr/bin/python3
import random
number = random.randint(-10, 10)


def signCheck(n):
    if (n > 0):
        print("{:d} is positive".format(n))
    elif (n < 0):
        print("{:d} is negative".format(n))
    else:
        print("{:d} is zero".format(n))
    return


signCheck(number)
