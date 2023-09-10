#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    """ Deletes the item at a specific position in a list.
        my_list: The input list from which to delete the item.
        idx (int): The index at which to delete the item. sets to 0.
    Returns:
        list: A new list with the item at the specified index removed.
        If idx is
              negative or out of range, it returns the same input list."""
    if idx >= 0 and idx < len(my_list):
        del my_list[idx]
    return (my_list)
