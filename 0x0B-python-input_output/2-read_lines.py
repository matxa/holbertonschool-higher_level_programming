#!/usr/bin/python3
"""Function to print n lines"""


def read_lines(filename="", nb_lines=0):
    """opens a file and print n
    amount of lines
    """
    with open('my_file_0.txt', 'r') as file:
        text = file.readlines()
    if nb_lines < 0 or len(text) < nb_lines:
        for line in text:
            print(line, end="")
    else:
        text = text[:nb_lines]
        for line in text:
            print(line, end="")
