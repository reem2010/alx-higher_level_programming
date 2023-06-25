def search_replace(my_list, search, replace):
    new_list = my_list.copy()
    new_list= list(map(lambda v: v.replace(search, replace), str(new_list)))
    return (new_list)
