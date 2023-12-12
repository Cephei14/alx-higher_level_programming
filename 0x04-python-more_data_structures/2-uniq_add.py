#!/usr/bin/python3
def uniq_add(my_list=[]):
    if not my_list:
        return 0
    unique = set()
    total = 0
    for num in my_list:
        if num not in unique:
            total += num
            unique.add(num)
    return total
