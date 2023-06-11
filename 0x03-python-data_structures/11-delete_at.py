#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    """delete item
    Args:
        my_list: list
        idx: index
    Returns:
        new list
    """
    if (idx < 0) or (idx >= len(my_list)):
        return (my_list)
    if idx == (len(my_list) - 1):
        my_list[-1:] = []
    else:
        my_list[idx:idx+1] = []
    return (my_list)
