#!/usr/bin/python3
"""sends a request to the URL and displays the value of the X-Request-Id"""
from urllib.request import urlopen
import sys

if __name__ == "__main__":
    with urlopen(sys.argv[1]) as response:
        try:
            print(response.headers.get("X-Request-Id"))
        except Exception as e:
            pass
