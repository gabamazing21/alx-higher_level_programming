#!/usr/bin/python3
"""
this is a decoder module
"""
import json


def from_json_string(my_str):
    """
    from_json_string:
    parameter: my_str(string)
    return: it return decode python object
    """
    return json.loads(my_str)
