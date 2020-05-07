#!/usr/bin/python3
def search_replace(my_list, search, replace):
    idx = []
    new_list = my_list.copy()
    for i in range(len(new_list)):
        if new_list[i] == search:
            idx.append(i)
    for b in range(len(idx)):
        new_list.pop(idx[b])
        new_list.insert(idx[b], replace)
    return new_list
