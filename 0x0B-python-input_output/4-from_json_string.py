#!/usr/bin/python3
# 6-from_json_string.py
"""module examines a JSON-to-object python data structure."""
import json


def from_json_string(my_str):
    """Returns the Python object(python data structure)
     rep of a JSON str."""
    return json.loads(my_str)
