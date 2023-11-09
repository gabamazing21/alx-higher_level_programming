#!/usr/bin/python3
def search_replace(my_list, search, replace):
    res = my_list.copy()
    for index, i in enumerate(res):
        if (i == search):
            res[index] = replace
    return res
