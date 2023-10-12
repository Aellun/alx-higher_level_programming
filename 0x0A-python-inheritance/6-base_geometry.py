#!/usr/bin/python3
"""This modules examine a base geometry class BaseGeometry."""


class BaseGeometry:
    """Represent base geometry class."""

    def area(self):
        """Not-implementederror: if the error not implemented
        sub-class."""
        raise Exception("area() is not implemented")
