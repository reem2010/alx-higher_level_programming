#!/usr/bin/python3
def print_list_integer(my_list=[]):
    """print list
    Args:
        my_list: list
    Returns:
        nothing
    """
    i = 0
    while i < len(my_list):
        print("{:d}".format(my_list[i]))
        i = i + 1
