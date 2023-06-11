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
    my_list[idx] = []
    return (my_list)
