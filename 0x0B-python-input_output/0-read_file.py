#!/usr/bin/python3
"""function read_file()"""


def read_file(filename=""):
    """read from a filename
    """
    with open('my_file_0.txt') as file:
        text = file.read()
        print(text, end="")