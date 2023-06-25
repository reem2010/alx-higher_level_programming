#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0;
    for i in range(len(my_list) - 1):
        print(i)
        if (my_list.count(my_list[i]) > 1):
            my_list.remove(my_list[i])
    for j in range(len(my_list) - 1):
        sum = sum + my_list[j]
