#!/usr/bin/python3
'''Check error code'''

from requests import get
from sys import argv as av
if __name__ == "__main__":
    response = get(av[1])
    status = response.status_code
    if status >= 400:
        print("Error code: {}".format(status))
    else:
        print(response.text)
