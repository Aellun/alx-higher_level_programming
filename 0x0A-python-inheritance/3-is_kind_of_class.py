#!/usr/bin/python3
"""this module establish an inherited class_checking function."""


def inherits_from(obj, a_class):
    """examines if an object is an inherited instance of a class.

    Args:
        obj (any): The object being checked
        a_class (type): The class to match the type of obj to.
    Returns:True If obj is an inherited instance of a_class
        Otherwise - False.
    """
    if isinstance(obj, a_class):
        return True
    return False
