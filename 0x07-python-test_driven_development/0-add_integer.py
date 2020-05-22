#!/usr/bin/python3


def add_integer(a, b=98):
    """Return the sum of a and b
    if a is not None and type is int or float
    """
    if a is None:
        raise TypeError("a must be an integer")
    if a * 0 != 0:
        raise TypeError("a must be an integer")
    else:
        a = int(a)
    if b * 0 != 0:
        raise TypeError("b must be an integer")
    else:
        b = int(b)
    return a + b
