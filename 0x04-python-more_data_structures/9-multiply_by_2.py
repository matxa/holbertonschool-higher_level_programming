#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    a_dictionary_copy = a_dictionary.copy()
    for k in a_dictionary_copy:
        a_dictionary_copy[k] = a_dictionary_copy[k] * 2
    return a_dictionary_copy
