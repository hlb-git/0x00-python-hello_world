#!/usr/bin/python3
"""define a rectangle"""


class Rectangle:
    """width and heigth attributes"""

    def __init__(self, width=0, heigth=0):
        self.width = width
        self.heigth = height

    @property
    def width(self):
        """gets width"""

        return self.__width

    @width.setter
    def width(self, value):
        """sets value"""

        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if width < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def heigth(self):
        """gets heigth"""

        return self.__heigth

    @heigth.setter
    def heigth(self, value):
        """sets heigth"""
        if not isinstance(value, int):
            raise TypeError('heigth must be an integer')
        if heigth < 0:
            raise ValueError('heigth must be >= 0')
        self.__heigth = value
