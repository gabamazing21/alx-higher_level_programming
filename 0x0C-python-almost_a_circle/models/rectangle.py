#!/usr/bin/python3
"""Rectangle Module"""
from models.base import Base


class Rectangle(Base):
    """Rectangle Class that inheirt Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize Rectangle"""
        if (type(width) is not int):
            raise TypeError("width must be an integer")
        if (type(height) is not int):
            raise TypeError("height must be an integer")
        if (type(x) is not int):
            raise TypeError("x must be an integer")
        if (type(y) is not int):
            raise TypeError("y must be an integer")
        if (width <= 0):
            raise ValueError("width must be > 0")
        if (height <= 0):
            raise ValueError("height must be > 0")
        if (x < 0):
            raise ValueError("x must be >= 0")
        if (y < 0):
            raise ValueError("y must be >= 0")

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """get width"""
        return self.__width

    @width.setter
    def width(self, width):
        """Set width"""
        if (type(width) is not int):
            raise TypeError("width must be an integer")
        if (width <= 0):
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """get height"""
        return self.__height

    @height.setter
    def height(self, height):
        """set height"""
        if (type(height) is not int):
            raise TypeError("height must be an integer")
        if (height <= 0):
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """get x"""
        return self.__x

    @x.setter
    def x(self, x):
        """set x"""
        if (type(x) is not int):
            raise TypeError("x must be an integer")
        if (x < 0):
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """get y"""
        return self.__y

    @y.setter
    def y(self, y):
        """set y"""
        if (type(y) is not int):
            raise TypeError("y must be an integer")
        if (y < 0):
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """ return area of rectangle """
        return self.__width * self.__height

    def display(self):
        """dsiplay rectangle standard output with #"""
        for _ in range(self.__y):
            for _ in range(self.__x):
                print(end=" ")
            print()
        for _ in range(self.__height):
            for _ in range(self.__width):
                print("#", end='')
            print()

    def __str__(self):
        """str give string representation of the class """
        return (f"[Rectangle] ({self.id})"
                f" {self.__x}/{self.__y} - {self.__width}/{self.__height}")

    def update(self, *args, **kwargs):
        """ update instance values"""
        if (args):
            for i, arg in args.item():
                if i == 0:
                    self.id = arg
                elif i == 1:
                    self.__width = arg
                elif i == 2:
                    self.__height = arg
                elif i == 3:
                    self.__x = arg
                elif i == 4:
                    self.__y = arg
                else:
                    break
        else:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'weight' in kwargs:
                self.__weight = kwargs['weight']
            if 'height' in kwargs:
                self.__height = kwargs['height']
            if 'x' in kwargs:
                self.__x = kwargs['x']
            if 'y' in kwargs:
                self.__y = kwargs['y']

    def to_dictionary(self):
        """to_dictionary """
       rect_dict =  {}
       rect_dict['id'] = self.id
       rect_dict['size'] = self.__size
       rect_dict['x'] = self.__x
       rect_dict['y'] = self.__y
       return rect_dict
