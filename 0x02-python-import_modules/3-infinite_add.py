#!/usr/bin/python3

if __name__ == "__main__":
    """return the arg addition."""
    import sys

total = 0
    for n in range(len(sys.argv) - 1):
        total += int(sys.argv[n + 1])
    print("{}".format(total))
