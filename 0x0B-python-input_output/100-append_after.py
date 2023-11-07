#!/usr/bin/python3
"""read and update file"""


def append_after(filename="", search_string="", new_string=""):
    """search and update with new_string"""
    with open(filename, mode="r", encoding="UTF-8") as a_file:
        all_lines = a_file.readlines()

    with open(filename, mode="w", encoding="UTF-8") as a_file:
        for line in all_lines:
            a_file.write(line)
            if search_string in line:
                a_file.write(new_string)
