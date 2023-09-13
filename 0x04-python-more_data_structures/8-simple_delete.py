#!/usr/bin/python3


"""function that deletes a key in a dictionary.
    key: argument will be always a string
    If a key doesn’t exist, the dictionary won’t change"""


def simple_delete(a_dictionary, key=""):
    if key in a_dictionary:
        del a_dictionary[key]
    return (a_dictionary)
