#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    args = dir(hidden_4)
    for i in args:
        if "__" != i[:2]:
            print(i)
