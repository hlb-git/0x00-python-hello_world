#!/usr/bin/python3
"""student class"""


class Student:
    """class student"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """return dict detail of the class"""
        return (self.__dict__)

    def reload_from_json(self, json):
        if (json):
            self.__dict__ = json
