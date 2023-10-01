#!/usr/bin/python3
"""takes in a URL, sends a request to
the URL and displays the body of the response"""
from urllib.request import urlopen
from urllib.error import URLError
import sys

if __name__ == "__main__":
    try:
        with urlopen(sys.argv[1]) as response:
            data = response.read()
            print(data.decode('utf-8'))
    except URLError as e:
        print(f"Error code: {e.code}")
