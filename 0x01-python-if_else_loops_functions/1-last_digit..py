#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)


def greaterLessThanFive(n):
    last_digit = n % 10
    s_num = str(last_digit)
    prefix = "Last digit of " + str(n) + " is " + s_num + " "
    if (last_digit > 5):
        print(prefix + "and is greater than 5")
        return
    if (last_digit < 5):
        print(prefix + "and is less than 6 and not 0")
        return
    print(prefix + "and is 0")
    return


greaterLessThanFive(number)
