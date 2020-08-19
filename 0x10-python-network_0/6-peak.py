#!/usr/bin/python3
""" Module that defines function find_peak
"""


def find_peak(list_of_integers):
    """ PeaK Finding """
    if len(list_of_integers) == 0:
        return None
    if len(list_of_integers) == 1:
        return list_of_integers[0]
    if len(list_of_integers) == 2:
        if list_of_integers[0] > list_of_integers[1]:
            return list_of_integers[0]
        else:
            return list_of_integers[1]

    if list_of_integers.count(list_of_integers[0]) == len(list_of_integers):
        return list_of_integers[0]

    if list_of_integers[0] > list_of_integers[1]:
        return list_of_integers[0]
    if list_of_integers[-1] > list_of_integers[-2]:
        return list_of_integers[-1]

    peak_lis = []
    for num in range(len(list_of_integers)):
        if list_of_integers[num] > list_of_integers[num - 1] and\
           list_of_integers[num] > list_of_integers[num + 1]:
            peak_lis.append(list_of_integers[num])
    return peak_lis[0]
