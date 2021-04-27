#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)


def greaterLessThanFive(n):
    last_digit = abs(n) % 10
    if n < 0:
        last_digit = last_digit * -1
    prefix = "Last digit of {:d} is {:d} ".format(n, last_digit)
    if (last_digit > 5):
        print(prefix + "and is greater than 5")
        return
    elif (last_digit < 5):
        print(prefix + "and is less than 6 and not 0")
        return
    print(prefix + "and is 0")
    return


greaterLessThanFive(number)
