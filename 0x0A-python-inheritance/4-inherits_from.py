#!/usr/bin/python3
"""Inheritance"""


def inherits_from(obj, a_class):
    """
    function checks if the object is an instance of a class that inherited
    from the specified class
    """
    return ((type(obj) != a_class) and isinstance(obj, a_class))
