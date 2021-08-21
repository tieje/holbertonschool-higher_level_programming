#!/usr/bin/python3
'''Search user api'''
from requests import post
from sys import av as av
if __name__ == '__main__':
    val = ''
    if len(av) > 1 and bool(av[1]):
        val = av[1]
    data = {'q': value}
    response = post('http://0.0.0.0:5000/search_user', data=data)
    try:
        json_body = response.json()
        if bool(json):
            print("[{}] {}".format(json_body["id"], json_body["name"]))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
