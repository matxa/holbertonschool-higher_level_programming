#!/usr/bin/python3
"""class Square that inherites from Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """class Square"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """string representation
        """
        tprint = (self.id, self.x, self.y, self.width)
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(*tprint)

    """Getting size"""
    @property
    def size(self):
        """get size
        """
        return self.width

    """Setting size"""
    @size.setter
    def size(self, value):
        """set size
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    """Update the square"""
    def update(self, *args, **kwargs):
        """Update
        """
        if args and len(args) != 0:
            self.id = args[0]
            if len(args) > 1:
                self.width = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        else:
            for k, v in kwargs.items():
                if k == "size":
                    self.width = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v
                elif k == "id":
                    self.id = v

    """return a to_dictionary Representation"""
    def to_dictionary(self):
        """return dict
        """
        return {
            'id': self.id,
            'size': self.width,
            'x': self.x,
            'y': self.y
        }
