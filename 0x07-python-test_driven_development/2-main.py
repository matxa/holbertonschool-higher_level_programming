#!/usr/bin/python3
matrix_divided = __import__('2-matrix_divided').matrix_divided

matrix = [
    [1, 2, 3],
    [4, 5, 7]
]
matrix_1 = [
    [1, 2, 3],
    [4, 5]
]
matrix_2 = [
    [1, 2, 3],
    [4, 5, 'd']
]
try:
    print(matrix_divided(matrix, 3))
except Exception as e:
    print(e)

try:
    print(matrix_divided(matrix_1, 3))
except Exception as e:
    print(e)

try:
    print(matrix_divided(matrix, 0))
except Exception as e:
    print(e)

print(matrix)
