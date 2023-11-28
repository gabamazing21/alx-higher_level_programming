#!/usr/bin/python3
class Rectangle:
    """
    Rectangle class
    """
    try:
        def __init__(self, width=0, height=0):
            self.__width = width
            self.__height = height

        def width(self):
            return self.width

        def width(self, value):
            if type(value) is not int:
                raise TypeError("width must be an integer")
            elif value < 0:
                raise ValueError("width must be >= 0")
            else:
                self.__width = value

        def height(self):
            return self.height

        def height(self, value):
            if type(value) is not int:
                raise TypeError("height must be an integer")
            elif value < 0:
                raise ValueError("height must be >= 0")
            else:
                self.height = value

    except TypeError as err:
        print(err)
    except ValueError as err:
        print(err)
    except Exception as err:
        print(err)
