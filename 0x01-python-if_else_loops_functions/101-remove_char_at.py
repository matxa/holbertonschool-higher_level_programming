#!/usr/bin/python3
def remove_char_at(str, n):
    if (n > len(str) or n < 0):
        return str
    to_be_replaced = str[n]
    new_str = str.replace(to_be_replaced, '', 1)
    return new_str
