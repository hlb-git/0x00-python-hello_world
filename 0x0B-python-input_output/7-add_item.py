#!/usr/bin/python3
"""load, add and save"""


import json
import sys


save_json = __import__('5-save_to_json_file').save_to_json_file
load_json = __import__('6-load_from_json_file').load_from_json_file
del (sys.argv[0])
save_json(sys.argv, "add_item.json")
print(load_json("add_item.json"))
