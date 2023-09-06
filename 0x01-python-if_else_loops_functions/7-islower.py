#!/usr/bin/python3
# 7-islower.py
def islower(c):
    """Check for lowercase char"""
    if ord('a') <= ord(c) <= ord('z'):
        return True
    else:
        return False
