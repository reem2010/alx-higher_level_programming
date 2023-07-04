#!/usr/bin/python3
"""adding two numbers module"""


def add_integer(a, b=98):
    """this function adds two nambers
    Args:
        a: first number
        b: second number
    Returns:
        summation of two numbers
    """
    if (type(a) != int) and (type(a) != float):
        raise TypeError("a must be an integer")
    if (type(b) != int) and (type(b) != float):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
