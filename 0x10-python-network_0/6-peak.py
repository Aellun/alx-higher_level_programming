#!/usr/bin/python3
"""function to  Find a peak in a list of unsorted integers
"""


def find_peak(list_of_integers):
    """
    Args:
    - list_of_integers: List of unsorted integers.

    Returns:
    - Peak integer.
    """
    size = len(list_of_integers)

    if size == 0:
        return None

    left, right = 0, size - 1

    while left < right:
        mid = (left + right) // 2

        # Check if the peak is on the left or right side
        if list_of_integers[mid] < list_of_integers[mid + 1]:
            left = mid + 1
        else:
            right = mid

    # At the end of the loop, left and right will be equal, representing a peak
    return list_of_integers[low]
