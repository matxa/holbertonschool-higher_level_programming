#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    # variables
    len = len(argv) - 1
    list_of_nums_to_sum = []
    # loop
    for i in range(1, len + 1):
        # append to list and do conversion
        list_of_nums_to_sum.append(int(argv[i]))
    print("{:d}".format(sum(list_of_nums_to_sum)))
