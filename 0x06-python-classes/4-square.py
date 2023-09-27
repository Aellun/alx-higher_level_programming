#!/usr/bin/python3
"""the module defines a class Square."""


class Square:
    """the class representing a square.
        Attributes:__size (int)
        Methods:__init__(self, size=0)"""

    def __init__(self, size=0):
        """Initializes an instance of a new Square.

        Args:
            size (int):New square size.
        """
        self.size = size

    @property
    def size(self):
        """Get the current size of the square."""
        return (self.__size)

    @size.setter
    """set the size of the square
        Args:
            value (int): The new size of the square. (a non-negative int.)
        Raises:
            TypeError: If the value is not an int.
            ValueError: If value < 0.
    """
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """int: Return the current area of the square."""
        return (self.__size * self.__size)
