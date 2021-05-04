#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    truthy = []
    for i in my_list:
        if i % 2 == 0:
            truthy.append(True)
        else:
            truthy.append(False)
    return truthy
