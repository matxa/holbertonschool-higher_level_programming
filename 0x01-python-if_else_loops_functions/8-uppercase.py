#!/usr/bin/python3
def uppercase(str):
    upp = 0
    for i in str:
        if ord(i) > 96:
            upp = ord(i) - 32
            print(chr(upp), end='')
        else:
            print(i, end='')
