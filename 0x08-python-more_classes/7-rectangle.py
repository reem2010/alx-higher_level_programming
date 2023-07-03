#!/usr/bin/python3
"""this module define rectangle class"""


class Rectangle:
    """rectangle class"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances = Rectangle.number_of_instances + 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """calculate the area
        Returns:
            the area
        """
        return (self.__width * self.__height)

    def perimeter(self):
        """calculate the perimeter
        Return:
            the perimeter
        """
        if self.__width == 0 or self.__height == 0:
            return (0)
        return (2 * (self.__width + self.__height))

    def __str__(self):
        string = ""
        if self.__width == 0 or self.__height == 0:
            return string
        for i in range(self.__height):
            for j in range(self.__width):
                string = string + str(self.print_symbol)
            if i != self.__height - 1:
                string = string + '\n'
        return string

    def __repr__(self):
        return (f"Rectangle({self.__width}, {self.__height})")

    def __del__(self):
        Rectangle.number_of_instances = Rectangle.number_of_instances - 1
        print("Bye rectangle...")
