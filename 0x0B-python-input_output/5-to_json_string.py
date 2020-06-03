#!/usr/bin/python3
"""JSON representation of an object"""
import json


def to_json_string(my_obj):
    """json to string
    returns string representation of
    Json
    """
    string_repr = json.dumps(my_obj)
    return string_repr
