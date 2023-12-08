#!/usr/bin/python3
"""
Say my name Module
"""


def say_my_name(first_name, last_name=""):
    """
    say_my_name print full name
    it takes two argurment first_name
    and last name string
    """
    if (first_name is None):
        raise TypeError("one argument missing")
    if (last_name is None):
        raise TypeError("one argument missing")
    if (first_name is None and last_name is None):
        raise TypeError("two argument missing")
    if (type(first_name) is not str):
        raise TypeError("first_name must be a string")
    if (type(last_name) is not str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
