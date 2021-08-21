#!/usr/bin/python3
'''Print github userid from github api'''
import requests
from requests.auth import HTTPBasicAuth
from sys import argv


if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    url = 'https://api.github.com/user'
    response = requests.get(url, auth=HTTPBasicAuth(username, password))
    info = response.json()
    print(info.get('id'))
