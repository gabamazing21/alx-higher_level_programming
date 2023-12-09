#!/usr/bin/python3
"""
Geometry module
"""


class BaseGeometry:
    """
    BaseGeometry
    class
    """
    def area(self):
        """for area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """integer_validator"""
        if (type(value) is not int):
            raise TypeError("must be an integer")
        if (value <= 0):
            raise ValueError("must be greater than 0")