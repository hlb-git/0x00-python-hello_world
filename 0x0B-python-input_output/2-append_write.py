#!/usr/bin/python3
"""append to a file"""


def append_write(filename="", text=""):
    """function to append"""
    with open(filename, mode="a", encoding="UTF-8") as a_file:
        return a_file.write(text)
