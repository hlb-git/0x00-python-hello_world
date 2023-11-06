#!/usr/bin/python3
""" check for instance """


def inherits_from(obj, a_class):
    """returns"""
    if type(obj) is a_class:
        return False
    return isinstance(obj, a_class)
