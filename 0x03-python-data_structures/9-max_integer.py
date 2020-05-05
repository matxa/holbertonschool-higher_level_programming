#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) <= 0:
        return None
    if my_list:
        new_ls = my_list.copy()
        new_ls.sort()
        return new_ls[-1]
