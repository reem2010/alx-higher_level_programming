#!/usr/bin/python3
"""Square mpdule"""
Rectangle = __import__('9-rectangle').Rectangle


class square(Rectangle):
    """Square class"""
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        return (self.__size * self.__size)
