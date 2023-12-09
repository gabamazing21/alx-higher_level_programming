#!/usr/bin/python3
"""
Module to check inheritance
"""


def inherits_from(obj, a_class):
    """
    this function
    check if it's a subclass
    """
    if (issubclass(type(obj), a_class)):
        if (isinstance(obj, a_class)):
            return True
        else:
            return False
    else:
        return False
