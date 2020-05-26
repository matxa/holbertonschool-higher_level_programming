#!/usr/bin/python3
"""add_integer add 2 integers"""


def add_integer(a, b=98):
    """Return the sum of a and b
    if a is not None and type is int or float
    """
    if a is None:
        raise TypeError("a must be an integer")
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(format((a + b), '.0f'))
