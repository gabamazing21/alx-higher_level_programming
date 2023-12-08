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
    found_space = False
    for j, i in enumerate(text):
        if (found_space):
            found_space = False
            continue
        print(i, end="")
        if (i == "." or i == "?" or i == ":"):
            print()
            print()
            if ((j < len(text)) and (text[j + 1] == " ")):
                found_space = True
