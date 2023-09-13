#!/usr/bin/python3


"""function that returns a key with the biggest integer value.
    values are only integers
    return: none if no score are found
    assume all student have different score"""


def best_score(a_dictionary):
    if not a_dictionary:
        return (None)

    return (max(a_dictionary, key=a_dictionary.get))
