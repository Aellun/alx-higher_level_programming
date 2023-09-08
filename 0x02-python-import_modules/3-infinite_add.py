#!/usr/bin/python3

if __name__ == "__main__":
    """Print the number of arg and list of arg."""
    import sys

    count = len(sys.argv) - 1
    if count == 0:
        print("Number of argument(s): 0.")
    elif count == 1:
        print("Number of argument(s): 1.")
    else:
        print("Number of argument(s): {}.".format(count))

    if count > 0:
        for n in range(count):
            print("{}: {}".format(n + 1, sys.argv[n+ 1]))

