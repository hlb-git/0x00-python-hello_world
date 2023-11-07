#!/usr/bin/python3
"""subclass my_int"""


class MyInt(int):
    """return logic checks"""

    def __init__(self, value):
        self.value = value

    def __eq__(self, another_value):
        return self.value != another_value

    def __ne__(self, another_value):
        return self.value == another_value
