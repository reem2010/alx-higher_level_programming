#!/usr/bin/python3
""" in this module we append to the file"""


def append_write(filename="", text=""):
    """append function"""
    with open(filename, "a") as file:
        file.write(text)
    return (len(text))
