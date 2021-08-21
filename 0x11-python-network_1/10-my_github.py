#!/usr/bin/python3
'''Print github userid from github api'''
from requests import get
from requests.auth import HTTPBasicAuth
from sys import av
if __name__ == "__main__":
    response = get('https://api.github.com/user', auth=HTTPBasicAuth(av[1], av[2]))
    try:
        json_body = response.json()
        print(json_body['id'])
    except:
        print('None')
