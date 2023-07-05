#!/usr/bin/python3
def text_indentation(text):
    """ prints a text
    Args:
        text: the text to be printed
    """
    if type(text) != str:
        raise TypeError("text must be a string")
    new = text.replace(". ", ".\n\n")
    new = new.replace("? ", "?\n\n")
    new = new.replace(": ", ":\n\n")
    print(new)
