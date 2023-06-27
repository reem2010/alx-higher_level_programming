#!/usr/bin/python3
"""this file contain the square class"""


class Square:
    """square class whth no arguments"""
    def __init__(self, size=0):
        try:
            if size < 0:
                raise ValueError("size must be >= 0")
        except TypeError:
            raise TypeError("size must be an integer")
        self.__size = size
        pass
    pass
