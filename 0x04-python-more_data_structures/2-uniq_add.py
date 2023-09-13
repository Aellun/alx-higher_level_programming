#!/usr/bin/python3
def uniq_add(my_list=[]):
    """function that adds all uniq int in a list once for each int."""
    uniq_list = set(my_list)
    uniq = 0

    for i in uniq_list:
        uniq += i

    return (uniq)
