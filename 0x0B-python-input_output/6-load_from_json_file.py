#!/usr/bin/python3
"""load a json encoded file"""


import json


def load_from_json_file(filename):
    """return an object"""
    with open(filename, mode="r", encoding="UTF-8") as a_file:
        return json.load(a_file)
