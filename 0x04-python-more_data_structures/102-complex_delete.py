#!/usr/bin/python3


"""function that deletes keys with a specific value in a dictionary.
    If the value does not exist, the dictionary will not change
    All keys having the searched value have to be deleted"""


def complex_delete(a_dictionary, value):
    key_list = list(a_dictionary.keys())

    for value_dic in key_list:
        if value == a_dictionary.get(value_dic):
            del a_dictionary[value_dic]

    return (a_dictionary)
