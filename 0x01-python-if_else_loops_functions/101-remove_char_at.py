#!/usr/bin/python3
def remove_char_at(str, n):
    """without the character at position n, a copy of the string is Created """
    if n < 0:
        return (str)
    return (str[:n] + str[n+1:])
