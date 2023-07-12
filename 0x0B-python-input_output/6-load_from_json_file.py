#!/usr/bin/python3
"""in this module a function that creates an Object from a “JSON file"""
import json


def load_from_json_file(filename):
    """creates an Object from a JSON file"""
    with open(filename, "r") as file:
        return (json.dumps(file.read()))

