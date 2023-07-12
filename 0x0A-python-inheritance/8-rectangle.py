#!/usr/bin/python3
"""Geometry module"""


class BaseGeometry:
    """Geometry class"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if (type(value) != int):
            raise TypeError(f"{name} must be an integer")
        if (value <= 0):
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """Rectangle class"""
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
