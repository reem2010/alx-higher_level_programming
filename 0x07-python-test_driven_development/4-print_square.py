#!/usr/bin/python3
"""in this module there is a print_square function"""
def print_square(size):
    """prints a square with the character #
    Args:
        size: size of the square
    """
    if (type(size) != int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)
