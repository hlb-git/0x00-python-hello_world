#!/usr/bin/python3
"""write to file using json encoding"""


import json


def save_to_json_file(my_obj, filename):
    """return json encoded file"""
    with open(filename, mode="w", encoding="UTF-8") as a_file:
        json.dump(my_obj, a_file)
