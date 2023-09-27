#!/usr/bin/python3
"""the module defines a class Square."""


class Square:
    """the class representing a square.
        Attributes:__size (int)
        Methods:__init__(self, size=0)"""

    def __init__(self, size=0):
        """Initializes an instance of a new Square.

        Args:
            size (int): new square size.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
