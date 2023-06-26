#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return  None
    b = list(a_dictionary.values())
    b.sort()
    for i in a_dictionary.keys():
        if a_dictionary[i] == b[-1]:
            return i
