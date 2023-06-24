#!/usr/bin/python3
def uppercase(str):
    """uppercase function
    Args:
        str: character
    Returns:
        uppercase
    """
    c = ''
    for i in range(len(str)):
        if (str[i] >= 'a') and (str[i] <= 'z'):
            c = chr(ord(str[i]) - 32)
        else:
            c = str[i]

        print("{}".format(c), end="")
    print("")
