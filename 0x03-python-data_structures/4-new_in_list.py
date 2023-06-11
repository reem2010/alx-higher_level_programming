#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """replace in a copy
    Args:
        my_list: the original list
        idx: index
        element: new element
    Returns:
        a copy of the list
    """
    c_list = my_list.copy()
    if (idx < 0) or (idx >= len(my_list)):
        return (c_list)
    c_list[idx] = element
    return (c_list)
