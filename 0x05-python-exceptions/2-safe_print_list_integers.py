#!/usr/bin/python3


def safe_print_list_integers(my_list=None, x=0):

    """Prints the first x ints from the list.

    Args:
        my_list (list): The list containing elements to be printed.
        x (int): The number of ints to print.

    Returns:
        The number of ints printed.
    """
    if my_list is None:
        my_list = []

    item_count = 0
    for item in my_list:
        if item_count >= x:
            break

        if isinstance(item, int):
            print("{:d}".format(item), end="")
            item_count += 1

    print()
    return item_count
