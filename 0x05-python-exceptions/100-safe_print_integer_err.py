#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    """Prints an int with "{:d}".format()or prints an err msg to stder
    Args:
        value: Any value (integer, string, etc.).

    Returns:
        bool: True if value is an integer and false if otherwise.
    """
    try:
        print("{:d}".format(int(value)))
        return True
    except ValueError as e:
        print(f"Exception: {e}", file=sys.stderr)
        return False
    except TypeError as e:

        print(f"Exception: {e}", file=sys.stderr)
        return False
