#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    if length > 0:
        first_chr = sentence[0]
    else:
        first_chr = None
    len_first = (length, first_chr)
    return len_first
