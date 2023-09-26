#!/usr/bin/python3

import sys


def safe_print_integer_err(value):
    """Prints an int with "{:d}".format() or prints an err msg to stderr.

    Args:
        value (int or str): The value to be printed.

    Returns:
        bool: True if value is an int and printed successfully
        False otherwise.
    """
    try:
        value_as_int = int(value)
        print("{:d}".format(value_as_int))
        return True
    except (TypeError, ValueError) as e:
        print(f"Exception: {e}", file=sys.stderr)
        return False
