#!/usr/bin/python3
"""pascal Triangle"""


def pascal_triangle(n):
    """pascal triangle
    return ls
    """
    row = [1]
    ls = []
    y = [0]
    ls.append(row)
    for x in range(n):
        row = [l + r for l, r in zip(row + y, y + row)]
        ls.append(row)
    return ls
