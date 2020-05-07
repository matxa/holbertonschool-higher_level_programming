#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = [row[:] for row in matrix]
    for a in new_matrix:
        for b in range(len(a)):
            a[b] *= a[b]
    return new_matrix
