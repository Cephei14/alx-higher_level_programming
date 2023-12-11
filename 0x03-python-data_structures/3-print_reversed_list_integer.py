#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    list_len = len(my_list)
    if list_len == 0:
        return None
    else:
        for i in my_list:
            print("{:d}".format(my_list[list_len - i]))
