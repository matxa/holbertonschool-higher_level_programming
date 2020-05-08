#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    keys_to_be_del = []
    if value not in a_dictionary.values():
        return a_dictionary
    for k, v in a_dictionary.items():
        if v == value:
            keys_to_be_del.append(k)
    for key in keys_to_be_del:
        if key in keys_to_be_del:
            a_dictionary.pop(key)
    return a_dictionary
