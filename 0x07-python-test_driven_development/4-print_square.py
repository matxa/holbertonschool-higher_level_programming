#!/usr/bin/python3


def print_square(size):
    if type(size) != int:
        raise TypeError("size must be an integer")

    if size >= 0:
        for line in range(size):
            for square in range(size):
                print("#", end="")
            print()
    else:
        raise ValueError("size must be >= 0")
