#!/usr/bin/python3
"""
this module
append text to existing file
"""


def append_write(filename="", text=""):
    """
    append_write - append text to file
    it take two argument
    """

    with open(filename, 'a', encoding="UTF-8") as f:
        return f.write(text)
