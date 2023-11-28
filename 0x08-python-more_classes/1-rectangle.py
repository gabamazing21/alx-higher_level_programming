#!/usr/bin/python3
class Rectangle:
    """ Rectangle Class """
    def __init__(self, width=0, height=0):
        """
        Initialize properties of a new
        rectangle
        Args:
            width (int): the width of a rectangle
            heigth (int): the height of a rectangle
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """ get width of rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """ set width of rectangle"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ get height """
        return self.__height

    @height.setter
    def height(self, value):
        """ set height """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
