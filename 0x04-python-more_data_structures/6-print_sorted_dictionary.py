#!/usr/bin/python3


""" function that prints a dictionary by ordered keys.
    Keys should be sorted by alphabetic order"""


def print_sorted_dictionary(a_dictionary):
    ordered_list = list(a_dictionary.keys())
    ordered_list.sort()
    for i in ordered_list:
        print("{}: {}".format(i, a_dictionary.get(i)))
