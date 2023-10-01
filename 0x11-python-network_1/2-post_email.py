#!/usr/bin/python3
"""takes in a URL and an email"""
from urllib.parse import urlencode
from urllib.request import urlopen
from urllib.request import Request
import sys

if __name__ == "__main__":
    data = {'email': sys.argv[2]}
    data = urlencode(data).encode('ascii')
    request = Request(sys.argv[1], data)
    with urlopen(request) as response:
        email = response.read()
        print(email.decode('utf-8'))
