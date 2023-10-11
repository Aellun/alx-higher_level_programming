#!/usr/bin/python3
"""this module examines a base geometry class BaseGeometry."""


class BaseGeometry:
    """Reprsent base geometry class."""

    def area(self):
        """Notimplementederror."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """this function Validate a param as an int.

        Args:
            name (str): The name of the param
            value (int): The param to validate.
        Raises:
            TypeError: If value is not an int.
            ValueError: If value is <= 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
