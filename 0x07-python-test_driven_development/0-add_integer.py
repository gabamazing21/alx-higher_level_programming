#!/usr/bin/python3
"""
Module to add integer

"""


def add_integer(a, b=98):
    """
    this function calculation addition of integer or float

    Parameters:
    a (int or float): first integer
    b (int or float): second integer

    Returns:
    int or float: the additon of argument
    """
    try:
        if (type(a) is not int and type(a) is not float):
            raise TypeError("a must be an integer")
        elif (type(b) is not int and type(b) is not float):
            raise TypeError("b must be an integer")
        elif (a + 1 == a):
            raise OverflowError("a is too large")
        elif (b + 1 == b):
            raise OverflowError("b is too large")
        elif (a is None and b is not None):
            raise SyntaxError("missing one argument")
        elif (a is not None and b is None):
            raise SyntaxError("missing one argument")
        elif (a is None and b is None):
            raise SyntaxError("missing two arguments")
        else:
            return int(a) + int(b)
    except TypeError as e:
        return str(e)
    except OverflowError as e:
        return str(e)
    except SyntaxError as e:
        return str(e)
