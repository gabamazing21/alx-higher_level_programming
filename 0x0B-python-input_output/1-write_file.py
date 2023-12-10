#!/usr/bin/python3
"""
This module
we work on how to write in python
"""


def write_file(filename="", text=""):
    """
    write_file - write to file
    it take two argument
    filename and text
    """
    with open(filename, 'w', encoding="UTF-8") as f:
        return f.write(text)
