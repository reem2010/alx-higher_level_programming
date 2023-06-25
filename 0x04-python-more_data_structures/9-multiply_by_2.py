#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    b = a_dictionary.copy()
    for i in b.keys():
        b.update({i: (b.get(i)) * 2})
    return (b)
