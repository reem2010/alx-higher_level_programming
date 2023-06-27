#!/usr/bin/python3
"""this file contain the square class"""


class Square:
    """square class whth no arguments"""
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        pass
    pass
