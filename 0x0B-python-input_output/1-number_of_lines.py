#!/usr/bin/python3
"""Function number_of_lines"""


def number_of_lines(filename=""):
    """return the number
    of lines in a text file
    """
    with open('my_file_0.txt', 'r') as file:
        text = file.readlines()
        return len(text)
