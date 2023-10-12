#!/usr/bin/python3
"""This module examine inherited list class MyList
    that implements sorted printing."""


class MyList(list):
    """Implements a sorted printing for the built-in list class.

    This class inherits from the built-in `list` class and adds a new method,
    `print_sorted()`, which prints the list in sorted ascending order.

    """

    def print_sorted(self):
        """Print a list in sorted ascending order.

        sorts the list in ascending order and then prints
        """
        print(sorted(self))
