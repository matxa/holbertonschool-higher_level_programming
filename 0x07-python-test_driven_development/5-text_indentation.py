#!/usr/bin/python3


def text_indentation(text):
    if type(text) != str:
        raise TypeError("text must be a string")

    list(text)
    text_cpy = []
    new_cpy = []
    where_to_add_new_line = ['.', '?', ':']
    for char in range(len(text)):
        if text[char] in where_to_add_new_line:
            text_cpy.append(text[char])
            text_cpy.append('~')
        else:
            text_cpy.append(text[char])

        str_1 = ""
        for char in text_cpy:
            str_1 += char
    for i in str_1.split("~ "):
        new_cpy.append(i)
    for a in new_cpy:
        if a != new_cpy[-1]:
            print("{}".format(a))
            print()
        else:
            print("{}".format(a), end="")
