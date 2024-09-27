#!/usr/bin/python3
"""square class module"""


class Square:
    """A class that defines a square with size valida
    tion and area calculation."""

    def __init__(self, size=0):
        """Initialize a new Square in
        stance with optional size validation.

        Args:
            size (int): The size of one s
            ide of the square (default is 0).

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")  
        if size < 0:
            raise ValueError("size must be >= 0")   
        self.__size = size  

    def area(self):
        """Calculate and return the current square area.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
