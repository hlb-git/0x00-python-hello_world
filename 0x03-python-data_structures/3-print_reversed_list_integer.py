#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    size = len(my_list)
    while size > 0:
        print("{}".format(my_list[size - 1]))
        size -= 1
