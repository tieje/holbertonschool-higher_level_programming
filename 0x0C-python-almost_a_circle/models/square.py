#!/usr/bin/python3
"""
A Square Boi
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Classy Square
    """

    def __init__(self, size, x=0, y=0, id=None):
        self.size = size
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """square details"""
        return "[{}] ({}) {}/{} - {}".format(
            __class__.__name__,
            self.id, self.x, self.y, self.size)
