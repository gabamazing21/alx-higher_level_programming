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

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string
        representation of list_objs
        to a file:"""
        file_name = "Rectangle.json"
        dict_list = []
        if list_objs is not None:
            for i in list_objs:
                shapes = i
                dictionary = shapes.to_dictionary()
                json_dictionary = cls.to_json_string(dictionary)
                dict_list.append(json_dictionary)
        with open(file_name, 'w', encoding="UTF-8") as f:
            f.write(str(dict_list))
