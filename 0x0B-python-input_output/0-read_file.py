#!/usr/bin/python3
"""function read_file()"""


def read_file(filename=""):
    """read from a filename
    """
    with open(filename, encoding="utf-8") as file:
        text = file.read()
    print(text, end="")
