#!/usr/bin/python3
def element_at(my_list, idx):
    lilen = len(my_list)
    if lilen < idx < 0:
        return "None"
    else:
        return my_list[idx]
