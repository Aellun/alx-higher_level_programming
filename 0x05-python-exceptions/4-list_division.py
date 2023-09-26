#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    """Divides 2 lists elelments.

    Args:
        my_list_1 (list): list 1.
        my_list_2 (list): list 2
        list_length (int): The number of elements to divide.

    Returns:
        A new list of length list_length containing all the divisions
        if indivisible result of division equals 0.
    """
    list_new = []
    for item in range(0, list_length):
        try:
            div = my_list_1[item] / my_list_2[item]
        except TypeError:
            print("wrong type")
            div = 0
        except ZeroDivisionError:
            print("division by 0")
            div = 0
        except IndexError:
            print("out of range")
            div = 0
        finally:
            list_new.append(div)
    return (list_new)
