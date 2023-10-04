#!/usr/bin/python3
"""This module defines a Rectangle class."""


class Rectangle:
    """Rep a rectangle."""

    def __init__(self, width=0, height=0):
        """Initializes a new Rectangle.

        Args:
            width (int): the new rectangle width
            height (int): new rectangle height
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get and or set the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get and or set the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the Rectangle area"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Returns the Rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the Rectangle with the max area.

        Args:
            rect_1: The 1st Rectangle.
            rect_2: The 2nd Rectangle.
        Raises:
            TypeError: If either of rect_1 or rect_2 is not a Rectangle.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        return (rect_2)

    @classmethod
    def square(cls, size=0):
        """Return a new Rectangle where width and height are = size.

        Args:
            size (int): The width and height of the new Rectangle.
        """
        return (cls(size, size))

    def __str__(self):
        """Returns rep of the Rectangle with the # character.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        rect = []
        for item in range(self.__height):
            [rect.append('#') for j in range(self.__width)]
            if item != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))

    def __repr__(self):
        """Returns the string rep of the Rectangle."""
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return (rect)

    def __del__(self):
        """Print a message for deletion of a Rectangle."""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
