#!/usr/bin/python3
"""write object to text file"""
import json


def save_to_json_file(my_obj, filename):
    """writes an Object to a text
    file, using a JSON representation
    """
    with open(filename, "w") as file:
        string_repr = json.dumps(my_obj)
        file.write(string_repr)
