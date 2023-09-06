#!/usr/bin/python3
# 8-uppercase.py
def uppercase(str):
    """Prints str the in uppercase."""
    for c in str:
        if ord(c) >= 97 and ord(c) <= 122:
            c = chr(ord(c) - 32)
        print(f"{c}", end="")
    else:
        print("")
