#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """print reversed list
    Args:
        my_list: the list
    """
    i = len(my_list) - 1
    while i >= 0:
        print("{:d}".format(my_list[i]))
        i = i - 1
