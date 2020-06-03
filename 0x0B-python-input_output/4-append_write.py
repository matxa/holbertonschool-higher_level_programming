#!/usr/bin/python3
"""function to append str"""


def append_write(filename="", text=""):
    """appends a string at the end of a
    text file (UTF8) and returns the number
    of characters added
    """
    with open(filename, 'a') as file:
        number_of_char = file.write(text)
    return number_of_char
