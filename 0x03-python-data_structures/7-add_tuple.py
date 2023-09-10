#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    """adds two tuples,return a tuple with 2 int, ensure tuple has 2 element"""
    """by adding 0 if necessary"""
    while len(tuple_a) < 2:
        tuple_a += (0,)
    while len(tuple_b) < 2:
        tuple_b += (0,)
    # adds the first 2 element of the tuple
    New_tuple = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])

    return New_tuple
