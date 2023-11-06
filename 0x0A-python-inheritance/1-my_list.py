#!/usr/bin/python3
""" print sorted list"""


class MyList(list):
    """ print sorted list"""
    def print_sorted(self):
        print(sorted(self))
