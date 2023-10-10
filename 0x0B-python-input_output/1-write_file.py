#!/usr/bin/python3
"""this module writes a  str to a text"""


def write_file(filename="", text=""):
    """Write a string to a UTF8 text file.

    Args:
        filename (str): the file name to write to
        text (str): The str to write
    Returns:
        The number of char written
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
