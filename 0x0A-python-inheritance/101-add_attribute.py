#!/usr/bin/python3
"""adds new attribute if possible"""


def add_attribute(obj, attr, value):
    """set attribute"""
    if (hasattr(obj, attr)):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, value)
