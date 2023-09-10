#!/usr/bin/python3

def no_c(my_string):
    """function that removes all characters c and C from str"""
    no_c_string = [s for s in my_string if s != 'c' and s != 'C']
    return ("".join(no_c_string))
