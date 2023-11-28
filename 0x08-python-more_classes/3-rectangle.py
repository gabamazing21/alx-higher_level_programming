#!/usr/bin/python3
"""Rectangle Classess"""
class Rectangle:
    """ Rectangle Class Representation """
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
    def area(self):
        """ get area of the rectangle"""
        return self.__height * self.__width
    def perimeter(self):
        """ get the perimeter of the rectangle """
        if (self.__height == 0 or self.__width == 0):
            return 0
        return (2 * self.__height) + (2 * self.__width)
    def __str___(self):
        if (self.__width == 0 or self.__height == 0):
            return ""
        return str([''.join(['#' for _ in range(self.__width)]) for _ in range(self.__height)])
