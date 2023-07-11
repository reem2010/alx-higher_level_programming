#!/usr/bin/python3
""" in this module we read the file"""


def read_file(filename=""):
    """read function"""
    with open(filename, "r") as file:
        print(file.read(), end="")
