#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for a in matrix:
        for b in range(len(a)):
            if a[b] != a[-1]:
                print("{:d}".format(a[b]), end=' ')
            else:
                print("{:d}".format(a[b]), end='')
        print()
