#!/usr/bin/python3
def search_replace(my_list, search, replace):
    def replacethis(x):
        if x == search:
            x = replace
        return x
    new_list = list(map(replacethis, my_list))
    return new_list
