#!/usr/bin/python3
"""this module examines an inherited class_checking function."""


def inherits_from(obj, a_class):
    """inspect if an object is an inherited instance of a class.

    Args:
        obj (any): The object to be inspected.
        a_class (type): The class to match the type of object to.
    Returns:True If an object is an inherited instance of a_class
        Otherwise - False.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
