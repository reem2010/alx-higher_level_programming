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

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value


    def area(self):
        """calculate the area
        Return:
            the area
        """
        return ((self.__size) ** 2)
    pass
