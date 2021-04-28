#!/usr/bin/python3
def remove_char_at(str, n):
    if n + 1 == 0:
        print(str[:n])
    else:
        print(str[:n] + str[n + 1:])
