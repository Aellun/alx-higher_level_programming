#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """function that replaces an element in list"""
    """ at a specific pstn not modifying the original list"""
    if idx < 0 or idx > (len(my_list) - 1):
        return my_list

    copy = list(my_list)
    copy[idx] = element
    return copy
