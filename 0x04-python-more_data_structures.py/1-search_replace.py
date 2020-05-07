#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if my_list:
        # idx will store the index of where to delete and insert new element
        idx = []
        # copy list so can maaintain the original
        new_list = my_list.copy()
        # iterating through the new_list, and checking at what index contain
        # the number equal to search
        for i in range(len(new_list)):
            if new_list[i] == search:
                idx.append(i)
        # iterating through idx list, deleting and adding to new_list
        for b in range(len(idx)):
            new_list.pop(idx[b])
            new_list.insert(idx[b], replace)
        return new_list
