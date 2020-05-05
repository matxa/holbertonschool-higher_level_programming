#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    reverse_my_list = my_list[::-1]
    for num in reverse_my_list:
        print("{:d}".format(num))
