#!/usr/bin/python3
from models.base import Base
"""rectangle module"""


class Rectangle(Base):
    """rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """initialize the attributes"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """get widthh"""
        return self.__width

    @width.setter
    def width(self, value):
        """set widthh"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """get height"""
        return self.__height

    @height.setter
    def height(self, value):
        """set height"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """get x"""
        return self.__x

    @x.setter
    def x(self, value):
        """set x"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """get y"""
        return self.__y

    @y.setter
    def y(self, value):
        """set y"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """tis function returns the area"""

        return (self.__width * self.__height)

    def display(self):
        """prints in stdout the Rectangle instance with the character #"""

        for i in range(self.__y):
            print("\n", end="")
        for i in range(self.__height):
            for k in range(self.__x):
                print(" ", end="")
            for j in range(self.__width):
                print("#", end="")
                if j == self.__width - 1:
                    print("\n", end="")

    def __str__(self):
        """verriding the __str__ method"""
        return (f"[Rectangle] ({self.id}) {self.__x}/{self.__y}\
 - {self.__width}/{self.__height}")

    def update(self, *args, **kwargs):
        """Update the class Rectangle"""

        fun = ["id", "width", "height", "x", "y"]
        i = 0
        for ar in args:
            arg = fun[i]
            setattr(self, arg, ar)
            i += 1
        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle"""

        dic = {'x': self.__x, 'y': self.__y, 'id': self.id}
        dic.update({'height': self.__height, 'width': self.__width})
        return (dic)
