vi #!/usr/bin/python3
"""this function examine dict description."""


def class_to_json(obj):
    """Return the dictionary rep of a simple data structure."""
    return obj.__dict__
