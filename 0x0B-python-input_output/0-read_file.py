#!/usr/bin/python3
"""reads and print file content"""


def read_file(filename=""):
    """print filename data"""
    if filename:
        with open(filename, mode="r", encoding="UTF-8") as a_file:
            for i in a_file:
                print(i, end="")
