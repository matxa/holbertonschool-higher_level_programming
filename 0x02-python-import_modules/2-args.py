#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    # variables
    len = len(argv) - 1
    s = ''
    punctuation = ':'
    # conditions
    if len != 1:
        s = 's'
    if len == 0:
        punctuation = '.'
    # printing
    print("{:d} argument{}{}".format(len, s, punctuation))
    for i in range(1, len + 1):
        print("{:d}: {}".format(i, argv[i]))
