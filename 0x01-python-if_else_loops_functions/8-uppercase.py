#!/usr/bin/python3
# 8-uppercase.py
def uppercase(s):
    """Print char in uppercase."""
    output = ""
    for c in s:
        if 'a' <= c <= 'z':
            output += f"{c.upper()}"
        else:
            output += f"{c}"
    print(output)
