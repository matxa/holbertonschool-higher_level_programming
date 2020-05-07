#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    uniq = set(my_list)
    uniq = list(uniq)
    for i in range(len(uniq)):
        sum += uniq[i]
    return sum
