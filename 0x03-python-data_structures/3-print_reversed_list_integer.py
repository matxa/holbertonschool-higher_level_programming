#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list:
        new_ls = my_list.copy()
        new_ls.reverse()
        for num in new_ls:
            print("{:d}".format(num))
