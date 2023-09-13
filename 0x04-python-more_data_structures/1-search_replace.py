#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """Replaces all occurrences of an element by another in a new list.
        my_list: the initial list
        search: the element to replace in the list
        replace: the new element"""
    list_new = list(map(lambda x: replace if x == search else x, my_list))
    return (list_new)
