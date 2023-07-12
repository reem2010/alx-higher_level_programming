#!/usr/bin/python3
"""in this there is a write function"""


def write_file(filename="", text=""):
    """write function"""
    with open(filename, "w") as file:
        file.write(text)
        return (file.tell())
