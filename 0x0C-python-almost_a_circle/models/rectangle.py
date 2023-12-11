#!/usr/bin/python3
"""Rectangle Module"""
from models.base import Base


class Rectangle(Base):
    """Rectangle Class that inheirt Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize Rectangle"""
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    def setWidth(self, width):
        """Set width"""
        self.__width = width

    def getWidth(self):
        """get width"""
        return self.__width

    def setHeight(self, height):
        """set height"""
        self.__height = height

    def getHeight(self):
        """get height"""
        return self.__height

    def getX(self):
        """get x"""
        return self.__x

    def setX(self, x):
        """set x"""
        self.__x = x

    def getY(self):
        """get y"""
        return self.__y

    def setY(self, y):
        """set y"""
        self.__y = y
