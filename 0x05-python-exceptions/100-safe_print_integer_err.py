#!/usr/bin/python3
import sys

def safe_print_integer_err(value):
    """Prints an integer and returns True if value is an integer, else False.

    Args:
        value: Any value (integer, string, etc.).

    Returns:
        bool: True if value is an integer and successfully printed, False otherwise.
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
