#!/usr/bin/python3
"""This module examine a class and inherited class function."""


def is_kind_of_class(obj, a_class):
    """Checks if an object is an instance or inherited instance of a class.

    Args:
        obj: the object being checked
        a_class (type):class being matched to an object
    Returns:
    True- if an object is an inherited class of the object
        Otherwise - False.
    """
    if isinstance(obj, a_class):
        return True
    return False
