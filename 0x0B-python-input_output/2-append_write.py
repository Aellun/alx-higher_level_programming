#!/usr/bin/python3
"""This module append str to a text file"""


def append_write(filename="", text=""):
    """Appends a str to the end of a UTF8 text file.

    Args:
        filename (str):filename to be appended
        text (str): The str to append to the file.
    Returns:
        The number of char appended.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
