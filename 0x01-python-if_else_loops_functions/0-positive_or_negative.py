#!/usr/bin/python3
import random
number = random.randint(-10, 10)


def signCheck(n):
    s_num = str(n)
    if (n > 0):
        print(s_num + " is positive")
    elif (n < 0):
        print(s_num + " is negative")
    else:
        print(s_num + "is zero")
    return


signCheck(number)
