#!/usr/bin/python3
"""Module for a text file insertion."""


def append_after(filename="", search_string="", new_string=""):
    """inserts a line of text to a file, after each line
    having a specific string

    Args:
        filename :filename to insert
        search_string: the str to search
        new_string: str to be inserted
    """
    text = ""
    with open(filename) as r:
        for line in r:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as w:
        w.write(text)
