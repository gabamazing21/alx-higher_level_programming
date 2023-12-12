#!/usr/bin/python3
"""Base Module"""
import json


class Base:
    """Base Class"""
    __nb_projects = 0

    def __init__(self, id=None):
        """Base Class Initialization"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_projects += 1
            self.id = Base.__nb_projects

    @staticmethod
    def to_json_string(list_dictionaries):
        """to_json_string - sterilize data"""
        if list_dictionaries is not None:
            return json.dumps(list_dictionaries)
        else:
            return "[]"
