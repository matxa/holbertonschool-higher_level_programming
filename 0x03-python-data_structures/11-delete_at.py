#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if my_list:
        if (idx > len(my_list) - 1) or (idx == -1):
            return my_list
        num_at_idx = my_list[idx]
        my_list.remove(num_at_idx)
        return my_list
