#!/usr/bin/python3
""" define class Square"""


class Square:
    """class with private size field"""
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):
        """sets value of __self from outside of the class"""
        if (type(value) is not int):
            raise TypeError('size must be an integer')
        if (value < 0):
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """returns the square of the current area"""
        return (self.__size**2)
