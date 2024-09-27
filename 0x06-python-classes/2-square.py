#!/usr/bin/python3
"""square class module"""


class Square:
    """A class that defines a square with size validation."""

    def __init__(self, size=0):
        """Initialize a new Square instance with size validation.

        Args:
            size (int): The size of one side of the square (default is 0).

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size  # Private instance attribute
