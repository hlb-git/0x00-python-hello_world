#!/usr/bin/python3
"""rectangle model"""


from models.base import Base


class Rectangle(Base):
    """compute rectange calculations"""
    def __init__(self, width, height, x=0, y=0, id=None):
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width_getter(self):
        return self.__width
    
    @width_getter.setter
    def width_setter(self, value):
        self.__width = value

    @property
    def height_getter(self):
        return self.__height
    
    @height_getter.setter
    def height_setter(self, value):
        self.__height = value

    @property
    def x_getter(self):
        return self.__x
    
    @x_getter.setter
    def x_setter(self, value):
        self.__x = value

    @property
    def y_getter(self):
        return self.__y
    
    @y_getter.setter
    def y_setter(self, value):
        self.__y = value

    