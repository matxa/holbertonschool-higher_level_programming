#!/usr/bin/python3
"""pascal Triangle"""


def pascal_triangle(n):
    """pascal triangle
    return ls
    """
    ls = []
    row = [1]
    if n <= 0:
        return ls
    y = [0]
    ls.append(row)
    for x in range(n - 1):
        row = [l + r for l, r in zip(row + y, y + row)]
        ls.append(row)
    return ls
