#!/usr/bin/python3
"""
This module helps to understand write/read and
opening of file in python
"""


def read_file(filename=""):
    """
    read_file: it open file for reading
    """
    with open(filename, 'r', encoding="UTF-8") as f:
        for line in f:
            print(line, end='')
