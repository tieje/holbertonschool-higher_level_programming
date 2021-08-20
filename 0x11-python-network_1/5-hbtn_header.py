#!/usr/bin/python3
'''Get response of header'''

from requests import get
from sys import argv as av
if __name__ == "__main__":
    print(get(av[1]).headers.get("X-Request-Id"))
