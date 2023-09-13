#!/usr/bin/python3


""" function that returns the weighted average of all integers tuple
    (<score>, <weight>)
    Return: 0 if the list is empty"""


def weight_average(my_list=[]):
    if not my_list:
        return 0

    weight = 0
    average = 0

    for tup in my_list:
        weight += tup[0] * tup[1]
        average += tup[1]

    return (weight / average)
