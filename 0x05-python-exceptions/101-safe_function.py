#!/usr/bin/python3

import sys


def safe_function(fct, *args):
    """Executes a function safely.

    Args:
        fct: ptr to the function to execute.
        args: Args to pass to the funct

    Returns: result of the call funct otherwise none if error
            err printed to the stderr"""
    try:
        result = fct(*args)
        return result
    except Exception as e:
        print(f"Exception: {e}", file=sys.stderr)
        return None
