#!/usr/bin/python3
"""write to a file"""


def write_file(filename="", text=""):
    """return written data length"""
    with open(filename, mode="w", encoding="UTF-8") as a_file:
        if filename and text:
            return (a_file.write(text))
