#!/usr/bin/python3
"""decode json file"""


import json


def from_json_string(my_str):
    """return deserialized json string"""
    return json.loads(my_str)
