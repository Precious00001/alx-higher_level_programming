#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = list(map(lambda w: replace if w == search else w, my_list))
    return (new_list)
