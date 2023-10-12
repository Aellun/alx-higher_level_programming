#!/usr/bin/python3
"""thin module examine a class MyInt that inherits from int."""


class MyInt(int):
    """Invert int operators == and !=.
    The `real` attribute of a `MyInt` object is the original `int` value that
    the `MyInt` object was created fr4m
"""

    def __eq__(self, value):
        """Override == opeartor with != behavior.
        Args:
            value (int): The original `int` value to create
            the `MyInt` object fr4m
            Returns:
            True if the two values are not equal, False otherwise."""
        return self.real != value

    def __ne__(self, value):
        """Override != operator with == behavior."""
        return self.real == value
