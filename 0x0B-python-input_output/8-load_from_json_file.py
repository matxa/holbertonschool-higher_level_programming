#!/usr/bin/python3
"""object from json file"""
import json


def load_from_json_file(filename):
    """creates an Object
    from a “JSON file”
    """
    with open(filename) as file:
        my_str = file.read()
        data = json.loads(my_str)
        return data
