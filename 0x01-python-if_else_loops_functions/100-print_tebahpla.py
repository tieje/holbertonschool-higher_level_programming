#!/usr/bin/python3
for i in range(122, 95, -1):
    if i % 2 == 0:
        a = chr(i)
    elif i % 2 == 1:
        a = chr(i - 32)
    print("{}".format(a), end="")
