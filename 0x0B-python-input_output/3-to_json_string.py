#!/usr/bin/python3
"""this module returns JSON rep."""
import json


def to_json_string(my_obj):
    """Returns the JSON representation of a string object."""
    return json.dumps(my_obj)
