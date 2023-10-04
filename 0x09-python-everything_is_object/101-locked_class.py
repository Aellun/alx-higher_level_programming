#!/usr/bin/python3
"""Defines locked-class."""


class LockedClass:
    """
    Prevents the user from instantiating new LockedClass attributes
    except for attributes called 'first_name'.
    """

    # Define __slots__ to specify allowed attributes
    __slots__ = ["first_name"]
