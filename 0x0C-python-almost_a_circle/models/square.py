#!/usr/bin/python3
""" class Square """
from models.rectangle import Rectangle


class Square(Rectangle):
    """class Square"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ get size """
        return self.width

    @size.setter
    def size(self, value):
        """ set size """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def __str__(self):
        tpr = (self.id, self.x, self.y, self.size)
        return "[Square] ({}) {:d}/{:d} - {:d}".format(*tpr)

    def update(self, *args, **kwargs):
        """ Update """
        if args and len(args) != 0:
            self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        else:
            for k, v in kwargs.items():
                if k == "size":
                    self.size = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v
                elif k == "id":
                    self.id = v

    def to_dictionary(self):
        """return dict
        """
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }
