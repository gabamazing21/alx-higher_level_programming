#!/usr/bin/python3
"""
Print square module
"""


def print_square(size):
    """
    print square
    taking one argument
    return it's
    square by multiplication of it's size
    """
    if (size is None):
        raise TypeError("one argument missing")
    if (type(size) is not int):
        raise TypeError("size must be an integer")
    if (size < 0):
        raise ValueError("size must be >= 0")
    if (type(size) is float and size < 0):
        raise TypeError("size must be an integer")
    if (size + 1 == size):
        raise OverflowError("size is too large")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
