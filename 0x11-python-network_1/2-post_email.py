#!/usr/bin/python3
'''
Send Post request with email as parameter
'''
import urllib.request as uresp
import urllib.parse as upar

from sys import argv
if __name__ == "__main__":
    url_request = argv[1]
    email_input = argv[2]
    data = upar.urlencode({'email': email_input})
    data = data.encode('utf-8')
    with uresp.urlopen(url_request, data=data) as response:
        print(response.read().decode('utf-8'))
