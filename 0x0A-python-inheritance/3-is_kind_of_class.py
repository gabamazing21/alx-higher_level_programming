#!/usr/bin/python3
"""
True Module
"""


def is_kind_of_class(obj, a_class):
    """
    method return true or false
    if obj is child or instance of
    class
    """
    if (isinstance(obj, a_class)):
        return True
    else:
        return False
