#!/usr/bin/python3
# 9-print_last_digit.py
def print_last_digit(number):
    """Prints and return the last digit of a number."""
    l_digit = abs(number) % 10
    print(l_digit, end="")
    return l_digit
