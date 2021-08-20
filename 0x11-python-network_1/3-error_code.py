#!/usr/bin/python3
'''
Script that accepts URL and display body
'''
import urllib.error as ue
import urllib.request as ur
from sys import argv as av

if __name__ == "__main__":
    url_request = av[1]
    try:
        with ur.urlopen(url_request) as response:
            print(response.read().decode('utf-8'))
    except ue.HTTPError as err:
        print("Error code: {}".format(err.code))
