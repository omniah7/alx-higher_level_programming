#!/usr/bin/python3
"""Square Module"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Square constructor"""
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """size property"""
        return self.__size

    @size.setter
    def size(self, s):
        self.width = s
        self.height = s
        self.__size = self.width

    def __str__(self):
        """str representation of the rectangle"""
        return f"[Square] ({self.id}) " \
            + f"{self.x}/{self.y} - {self.width}"

    def update(self, *args, **kwargs):
        """assigns attributes (id - size - x - y)"""
        if len(args) == 0:
            for k, v in kwargs.items():
                # if hasattr(self, k):
                setattr(self, k, v)
        else:
            try:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]
            except IndexError:
                pass

    def to_dictionary(self):
        """ returns the dictionary representation of a Square"""
        return {'id': self.id,
                'size': self.size,
                'x': self.x,
                'y': self.y}
