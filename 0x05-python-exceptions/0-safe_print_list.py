#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """Print x elememts of a list.

    Args:
        my_list (list): The list containing element to be printed
        x (int): The number of elements to print from my_list.

    Returns:
        The actual element to be printed
    """
    count = 0
    for item in range(x):
        try:
            print("{}".format(my_list[item]), end="")
            count += 1
        except IndexError:
            break
    print("")
    return (count)
