#!/usr/bin/python3
def magic_string(string=[0]):
    string[0] += 1
    return ("Holberton, " * string[0])[0:len("Holberton, " * string[0]) - 2]
