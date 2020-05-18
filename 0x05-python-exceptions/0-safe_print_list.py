#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        len = 0
        for i in my_list[:x]:
            print("{}".format(i), end='')
            len += 1
        print()
        return len
    except:
        return len
