#!/usr/bin/python3
"""This module Defines a class and inherited class_checking function."""


def is_kind_of_class(obj, a_class):
    """Checks if an object is an instance or inherited instance of a class.

    Args:
        obj (any): the object to be inspected
        a_class (type): The class to match the type of obj to.
    Returns:
       True: If obj is an instance or inherited instance of a_class
        Otherwise - False.
    """
    if type(obj) == a_class:
        return True
    return False
