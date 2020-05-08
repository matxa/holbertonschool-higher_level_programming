#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    tuple_1_idx = []
    tuple_mul = []
    for l in my_list:
        for t in range(len(l)):
            tuple_1_idx.append(l[1])
            tuple_mul.append(l[0] * l[1])
            break
    total = sum(tuple_mul) / sum(tuple_1_idx)
    return total
