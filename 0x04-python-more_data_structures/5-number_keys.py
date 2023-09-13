#!/usr/bin/python3


def number_keys(a_dictionary):
    """function that returns the number of keys in a dictionary."""
    key_num = 0
    list_keys = list(a_dictionary.keys())

    for i in list_keys:
        key_num += 1

    return (key_num)
