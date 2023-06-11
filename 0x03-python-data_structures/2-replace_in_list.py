#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    """replace elemen in the list
    Args:
        my_list: the list
        idx: index
        element: new element
    Returns:
        the new list
    """
    if (idx < 0) or (idx >= len(my_list)):
        return (my_list)
    my_list[idx] = element
    return (my_list)
