#!/usr/bin/python3
"""the module defines a class Square."""


class Square:
    """the class representing a square.
        Attributes: __size (int)
        Methods: __init__(self, size=0)"""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes an instance of a new Square.

        Args:
            size (int): New square size.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get/set the current size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Get and or set the current size of the square."""
        return (self.__position)

    @position.setter
    def position(self, value):
        """Set the size of the square.

        Args:
            value (int): The new size of the square (a non-negative int).
        Raises:
            TypeError: If the value is not an int.
            ValueError: If value < 0.
        """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return: int- the current area of the square."""
        return (self.__size * self.__size)

    def my_print(self):
        """Prints the square with the # character based on its pstn and size
            returns:None and if size = 0 prints empty line"""
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")

    def __str__(self):
        """Define the print() representation of a Square."""
        if self.__size != 0:
            [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            if i != self.__size - 1:
                print("")
        return ("")
