#!/usr/bin/python3
"""base module"""
import json


class Base:
    """base clase for all other classes"""


    __nb_objects = 0
    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """Dictionary to JSON string"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return ("[]")
        return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        from models.rectangle import Rectangle
        out = []
        if cls is Rectangle:
            name = "Rectangle.json"
        else:
            name = "Square.json"
        if ((list_objs) is not None):
            for obj in list_objs:
                out.append(obj.to_dictionary())
            out = cls.to_json_string(out)
        with open(name, "w") as file:
            file.write(out)

    @classmethod
    def from_json_string(json_string):
        out = []
        if json_string is not None:
            return
