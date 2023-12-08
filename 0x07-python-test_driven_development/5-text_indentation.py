#!/usr/bin/python3

"""
Text Indentation Module
"""


def text_indentation(text):
    """
    text_indentation print 2 new lines
    after character like
    .,?:
    it takes strings only
    return nothing
    """
    if (text is None):
        raise TypeError("argument missing")
    if (type(text) is not str):
        raise TypeError("text must be a string")

    for i in text:
        print(i, end="")
        if (i == "." or i == "?" or i == ":"):
            print()
            print()
