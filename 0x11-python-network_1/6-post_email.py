#!/usr/bin/python3
from requests import post
from sys import argv as av
import seleneium

if __name__ == "__main__":
    data = {"email": av[2]}
    print(post(argv[1], data=data).text)
