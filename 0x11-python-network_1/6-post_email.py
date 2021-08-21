#!/usr/bin/python3
'''Post email'''

from requests import post
from sys import argv as av
if __name__ == "__main__":
    data = {"email": av[2]}
    print(post(av[1], data=data).text)
