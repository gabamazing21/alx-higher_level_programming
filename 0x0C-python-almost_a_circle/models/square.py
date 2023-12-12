#!/usr/bin/python3
""" Square Module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""
    def __init__(self, size, x=0, y=0, id=None):
        self.id = id
        self.__size = size
        self.__x = x
        self.__y = y
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ size getter"""
        return self.__size

    @size.setter
    def size(self, size):
        """ size setter"""
        if (type(size) is not int):
            raise TypeError("width must be an integer")
        if (size <= 0):
            raise ValueError("width must be > 0")
        self.__size = size
        self__weight = size
        self.__height = size

    def __str__(self):
        """string representation"""
        return (f"[Square] ({self.id}) {self.__x} /"
                f"{self.__y} - {self.__size}")

    def update(self, *args, **kwargs):
        """ update square value"""
        if (args):
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                elif i == 1:
                    self.__size = arg
                elif i == 2:
                    self.__x = arg
                elif i == 3:
                    self.__y = arg
                else:
                    break
        else:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'size' in kwargs:
                self.__size = kwargs['size']
            if 'x' in kwargs:
                self.__x = kwargs['x']
            if 'y' in kwargs:
                self.__y = kwargs['y']

    def to_dictionary(self):
        """to_dictionary return dictionary representaton of the object"""
        rect_dict = {}
        rect_dict['id'] = self.id
        rect_dict['size'] = self.__size
        rect_dict['x'] = self.__x
        rect_dict['y'] = self.__y
        return rect_dict
