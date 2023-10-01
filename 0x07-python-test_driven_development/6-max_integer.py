#!/usr/bin/python3
"""This Module finds the max int in a list
"""


def max_integer(list=[]):
    """The Function to find and return the max int in a list of ints
       Retun: None,  If the list is empty
    """
    if len(list) == 0:
        return None
    Max_result = list[0]
    i = 1
    while i < len(list):
        if list[i] > Max_result:
            Max_result = list[i]
        i += 1
    return Max_result
