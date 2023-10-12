#!/usr/bin/python3
"""This module defines an object attribute lookup function."""


def lookup(obj):
    """Returns  object list available attributes.

    Args:
        obj: The inspected object

    Returns:
        A list of str for object's available attributes representation.
    """

    attributes = dir(obj)

    return attributes
