#!/usr/bin/python3
"""empty class"""


class BaseGeometry:
    """ geaometry class"""

    def area(self):
        """raise an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validate attributes"""
        if not isinstance(value, int):
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))


"""subclass Rectangle"""


class Rectangle(BaseGeometry):
    """computes Rectangle shape"""

    def __init__(self, width, height):
        if not super().integer_validator("width", width):
            self.__width = width
        if not super().integer_validator("height", height):
            self.__height = height

    def area(self):
        """return arear of rectangle"""
        return self.__height * self.__width

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
