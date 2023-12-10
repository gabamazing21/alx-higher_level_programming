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
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        super().integer_validator("width", width)
        super().integer_validator("height", height)
