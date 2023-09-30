#!/usr/bin/python3
"""script that fetches https://alx-intranet.hbtn.io/status"""
from urllib.request import urlopen
import sys

if __name__ == "__main__":
    with urlopen(sys.argv[1]) as response:
        try:
            print(response.header.get("X-Request-Id"))
        except Exception as e:
            pass
