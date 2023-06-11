#!/usr/bin/python3
def no_c(my_string):
    """replace letter c
    Args:
        my_string: the string
    Returns:
        new string
    """
    i = 0
    new = ""
    while i < len(my_string):
        if my_string[i] != 'c' and my_string[i] != 'C':
            new = new + my_string[i]
        i = i + 1
    return (new)
