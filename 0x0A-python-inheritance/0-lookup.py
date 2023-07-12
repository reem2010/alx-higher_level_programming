#!/usr/bin/python3
"""returns the list of available attributes"""


def lookup(obj):
    """ returns the list of available attributes and methods of an object"""
    print(list(dir(obj)))
