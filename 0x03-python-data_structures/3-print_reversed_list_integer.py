#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    """in reverse order the function Prints all integers of a list"""
    if isinstance(my_list, list):
        my_list.reverse()
        for n in my_list:
            print("{:d}".format(n))