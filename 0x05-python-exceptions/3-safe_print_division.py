#!/usr/bin/python3

def safe_print_division(a, b):
    """ devide two integers
    a and b: the two integers to be divided
    Returns the division of a by b and otherwise none"""
    try:
        div = a / b
    except (TypeError, ZeroDivisionError):
        div = None
    finally:
        print("Inside result: {}".format(div))
    return (div)
