#!/usr/bin/python3
def islower(c):
    """lower case function
    Args:
        c: character to be checked
    Returns:
        True if c is lowercase
    """
    if (ord(c) >= 97) and (ord(c) <= 122):
        return (True)
    else:
        return (False)
