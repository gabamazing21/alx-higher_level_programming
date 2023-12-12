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

    def __str__(self):
        """string representation"""
        return (f"[Square] ({self.id}) {self.__x} /"
                f"{self.__y} - {self.__size}")
