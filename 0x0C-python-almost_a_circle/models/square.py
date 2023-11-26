#!/usr/bin/python3
"""square module"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """computes square properties"""

    def __init__(self, size, x=0, y=0, id=None):
        """class constructor for square"""
        super().__init__(size, size, x, y, id)
        self.height = size
        self.width = size

    def __str__(self):
        return ("[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                     self.y, self.width))

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):

        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """updates the attributes"""
        if args:
            i = 0
            for c in args:
                attr = ["id", "size", "x", "y"]
                setattr(self, attr[i], c)
                i += 1
        else:
            if kwargs:
                for key, Value in kwargs.items():
                    setattr(self, key, Value)

    def to_dictionary(self):
        dict = {'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y}
        return dict
