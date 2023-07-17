#!/usr/bin/python3
from models.rectangle import Rectangle
"""square module"""


class Square(Rectangle):
    """square class"""

    def __init__(self, size, x=0, y=0, id=None):

        super().__init__(size, size, x, y, id)

    def __str__(self):
        return (f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}")

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        fun = ["id", "size", "x", "y"]
        i = 0
        for ar in args:
            arg = fun[i]
            setattr(self, arg, ar)
            i += 1
        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dictionary(self):
        dic = {'id': self.id, 'x': self.x, 'size': self.height, 'y': self.y}
        return (dic)
