#!/usr/bin/python3
import urllib.request as ur
'''Fetch https://intranet.hbtn.io/status'''

if __name__ == "__main__":
    with ur.urlopen('https://intranet.hbtn.io/status') as u:
        body = u.read()
        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode('utf-8')))
