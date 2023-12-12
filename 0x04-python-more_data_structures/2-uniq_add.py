#!/usr/bin/python3
def uniq_add(my_list=[]):
    if not my_list:
        return None
    unique = set()
    total = 0
    for num in my_list:
        if num not in unique:
            total += num
            unique.add(num)
    return total
