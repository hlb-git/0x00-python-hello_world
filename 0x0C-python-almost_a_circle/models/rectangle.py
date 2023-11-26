#!/usr/bin/python3
"""rectangle model"""


from models.base import Base


class Rectangle(Base):
    """compute rectange calculations"""
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be > 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be > 0")
        self.__y = value

    def area(self):
        return self.height * self.width

    def display(self):
        print("\n" * self.y, end="")
        for x in range(self.height):
            print(' ' * self.x, end="")
            print("#" * self.width)

    def __str__(self):
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y,
                                                         self.width, self.height))

    def update(self, *args, **kwargs):
        if args:
            i = 0
            atrbs = ["id", "width", "height", "x", "y"]
            for a in args:
                setattr(self, atrbs[i], a)
                i += 1
        if kwargs:
            for j, k in kwargs.items():
                setattr(self, j, k)

    def to_dictionary(self):
        dict = {'id': self.id, 'width': self.width, 'height': self.height, 'x': self.x,
                 'y': self.y}
        return dict
