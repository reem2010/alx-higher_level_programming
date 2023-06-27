#!/usr/bin/python3
"""this file contain the square class"""


class Square:
    """square class whth no arguments"""
    def __init__(self, size=0, position=(0, 0)):
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        if type(position[0]) != int or type(position[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        return self.__posisition

    @position.setter
    def position(self, value):
        if type(value[0]) != int or type(value[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """calculate the area
        Return:
            the area
        """
        return ((self.__size) ** 2)

    def my_print(self):
        """prints in stdout the square with the character #"""
        if self.__size == 0:
            print("")
        for i in range(self.__position[1]):
            print("")
        for i in range(self.__size):
            for i in range(self.__position[0]):
                print(" ", end="")
            for j in range(self.__size):
                print("#", end="")
            print("")
    pass
