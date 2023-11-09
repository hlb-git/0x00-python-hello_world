#!/usr/bin/python3
"""base class for all other classes"""


class Base:
    """id creation module"""

    __nb_objects = 0

    def __init__(self, id=None):
        if id != None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
