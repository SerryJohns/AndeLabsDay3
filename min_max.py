def find_max_min(my_list):
    if min(my_list) == max(my_list):
        return [min(my_list)]
    return [min(my_list), max(my_list)]
