#!/usr/bin/python3
def matrix_divided(matrix, div):
    """
    matrix_divided() - divides all elements of a matrix.
    matrix: matrix list
    div: number to divide each element in the matrix
    Return: a new list matrix
    """
    if type(matrix) != list:
        raise TypeError(type_err)
    for lis in matrix:
        if type(lis) != list:
            raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")
        for num in lis:
            if num * 0 != 0:
                raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")
    sum_l = sum(len(row) for row in matrix)
    num_div = sum_l / len(matrix[0])
    if num_div.is_integer() is False:
        raise TypeError("Each row of the matrix must have the same size")
    if div * 0 != 0:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = [row[:] for row in matrix]
    for a in new_matrix:
        for b in range(len(a)):
            a[b] = round(a[b] / div, 2)
    return new_matrix
