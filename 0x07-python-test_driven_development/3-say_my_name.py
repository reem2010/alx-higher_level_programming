#!/usr/bin/python3
"""in this module a function that print athe name"""


def say_my_name(first_name, last_name=""):
    """print the name
    Args:
        first_name: first name
        last_name: last name
    """
    if (type(first_name) != str):
        raise TypeError("first_name must be a string")
    if (type(last_name) != str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
