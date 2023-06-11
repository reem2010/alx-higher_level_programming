#!/usr/bin/python3
def element_at(my_list, idx):
    """get element from list at index
    Args:
        my_list: list
        idx: the index
    Returns:
        the element
    """
    if (idx < 0) or (idx >= len(my_list)):
        return ("None")
    return (my_list[idx])
