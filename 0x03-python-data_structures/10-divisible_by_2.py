#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    """Find all multiples of 2 in a list
    returns: new list with "True" or "False"."""
    Divisible = []
    for n in range(len(my_list)):
        if my_list[n] % 2 == 0:
            Divisible.append(True)
        else:
            Divisible.append(False)

    return (Divisible)
