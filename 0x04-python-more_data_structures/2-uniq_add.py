#!/usr/bin/python3
def uniq_add(my_list=[]):
    my_set=set()
    result = 0
    for i in my_list:
        my_set.add(i)
    for j in my_set:
        result += j
    return (result)
