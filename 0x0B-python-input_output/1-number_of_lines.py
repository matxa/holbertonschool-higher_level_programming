#!/usr/bin/python3
"""Function number_of_lines"""


def number_of_lines(filename=""):
    """return the number
    of lines in a text file
    """
    with open(filename, encoding="utf-8") as file:
        text = file.readlines()
    return len(text)
