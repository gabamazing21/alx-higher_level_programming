#!/usr/bin/python3
"""Base Module"""


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
