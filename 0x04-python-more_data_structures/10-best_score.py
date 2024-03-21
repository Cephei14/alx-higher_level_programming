#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is not None:
        number = len(a_dictionary.values())
        if number > 0:
            result = max(a_dictionary.values())
            for i in a_dictionary.keys():
                if a_dictionary[i] == result:
                    return i
    return None
