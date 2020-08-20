#!/usr/bin/python3
"""Find Peak by basically using binary search
"""


def find_peak_helper(arr, low, high, n):
    """ Helper function """
    mid = low + (high - low)/2
    mid = int(mid)
    if ((mid == 0 or arr[mid - 1] <= arr[mid]) and
       (mid == n - 1 or arr[mid + 1] <= arr[mid])):
        return mid
    elif (mid > 0 and arr[mid - 1] > arr[mid]):
        return find_peak_helper(arr, low, (mid - 1), n)
    else:
        return find_peak_helper(arr, (mid + 1), high, n)


def find_peak(list_of_integers):
    """ Find Peak """
    if len(list_of_integers) <= 0:
        return None
    size = len(list_of_integers)
    index = find_peak_helper(list_of_integers, 0, size - 1, size)
    return list_of_integers[index]
