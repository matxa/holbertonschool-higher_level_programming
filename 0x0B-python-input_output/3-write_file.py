#!/usr/bin/python3
"""Function to write to file"""


def write_file(filename="", text=""):
    """writes a string to a text file (UTF8)
    and returns the number of characters written
    """
    with open(filename, 'w') as file:
        number_of_char = file.write(text)
    return number_of_char
