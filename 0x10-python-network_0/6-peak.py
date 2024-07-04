#!/usr/bin/python3
"""
Module to find a peak element in a list of unsorted integers.
"""

def find_peak(list_of_integers):
    """
    Finds a peak element in a list of unsorted integers.
    A peak element is an element that is greater than or equal to its neighbors.

    Args:
        list_of_integers (list): A list of unsorted integers.

    Returns:
        int: A peak element from the list. None if the list is empty.
    """
    if not list_of_integers:
        return None

    def binary_search_peak(arr, low, high):
        """
        Helper function to perform a binary search for the peak element.

        Args:
            arr (list): The list of integers.
            low (int): The lower index of the current sublist.
            high (int): The upper index of the current sublist.

        Returns:
            int: A peak element from the list.
        """
        if low == high:
            return arr[low]

        mid = (low + high) // 2

        if arr[mid] < arr[mid + 1]:
            return binary_search_peak(arr, mid + 1, high)
        else:
            return binary_search_peak(arr, low, mid)

    return binary_search_peak(list_of_integers, 0, len(list_of_integers) - 1)
