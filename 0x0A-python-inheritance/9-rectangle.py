#!/usr/bin/python3
"""
this module works wiht
Rectangle
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
        if (name is None):
            raise TypeError("missing one argument")
        if (value is None):
            raise TypeError("missing one argument")
        if (value is None and name is None):
            raise TypeError("missing two arguments")
        if (type(value) is not int):
            raise TypeError(f"{name} must be an integer")
        if (value <= 0):
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """
    Rectangle inherit from BaseGeometry
    """
    def __init__(self, width, height):
        """initialization of the class """
        self.__width = width
        self.__height = height
        super().integer_validator("width", width)
        super().integer_validator("height", height)

    def area(self):
        """ area return area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """return the representation of the class"""
        return f"[Rectangle] {self.__width}/{self.__height}"
