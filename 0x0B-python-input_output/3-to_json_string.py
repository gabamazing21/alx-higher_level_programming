#!/usr/bin/python3
import json
"""
this module
we work with json file
"""


def to_json_string(my_obj):
    """
    to_json_string - it json object
    parameter: my_obj
    it return json object
    """
    return json.dumps(my_obj)
