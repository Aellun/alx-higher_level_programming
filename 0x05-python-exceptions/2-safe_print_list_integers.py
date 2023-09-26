#!/usr/bin/python3

from itertools import count


def safe_print_list_integers(my_list=[], x=0):
    """Prints the first elemet of list

    Args:
        my_list (list): The list containing element to be printed
        x (int): The number of elements in my_list to be printed

    Returns:
        The number of elements printed.
    """
    count = 0
    for item in range(0, x):
        try:
            print("{:d}".format(my_list[item]), end="")
            count += 1
        except (ValueError, TypeError):
            continue
    print("")
    return (count)
