#!/usr/bin/python3
"""in tis module a print function is defined"""


def text_indentation(text):
    """ prints a text
    Args:
        text: the text to be printed
    """
    if type(text) != str:
        raise TypeError("text must be a string")
    new = text.replace(". ", ".").replace(".", ".\n\n")
    new = new.replace("? ", "?").replace("?", "?\n\n")
    new = new.replace(": ", ":").replace(":", ":\n\n")
    print(new)
