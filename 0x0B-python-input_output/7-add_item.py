#!/usr/bin/python3
"""load, add and save"""


import json
import sys


save_json = __import__('5-save_to_json_file').save_to_json_file
load_json = __import__('6-load_from_json_file').load_from_json_file

try:
    j_list = load_json("add_item.json")
except:
    j_list = []

for i in sys.argv[1:]:
    j_list.append(i)
save_json(j_list, "add_item.json")
