#!/usr/bin/python3
"""This module writes object to text file"""
import json


def save_to_json_file(my_obj, filename):
    """Writes an object to a text file using JSON rep."""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
