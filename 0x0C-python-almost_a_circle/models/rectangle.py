#!/usr/bin/python3
"""Rectangle Module"""


from models.base import Base


class Rectangle(Base):
    """Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Rectangle constructor"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """width property"""
        return self.__width

    @width.setter
    def width(self, w):
        if type(w) is not int:
            raise TypeError("width must be an integer")
        if w <= 0:
            raise ValueError("width must be > 0")
        self.__width = w

    @property
    def height(self):
        """height property"""
        return self.__height

    @height.setter
    def height(self, h):
        if type(h) is not int:
            raise TypeError("height must be an integer")
        if h <= 0:
            raise ValueError("height must be > 0")
        self.__height = h

    @property
    def x(self):
        """x property"""
        return self.__x

    @x.setter
    def x(self, x):
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """y property"""
        return self.__y

    @y.setter
    def y(self, y):
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """returns the area value of the Rectangle instance"""
        return self.width * self.height

    def display(self):
        """ prints in stdout the Rectangle instance
        with the character #"""
        print('\n' * self.y, end='')
        for i in range(self.height):
            row = ' ' * self.x + "#" * self.width
            print(row)

    def __str__(self):
        """str representation of the rectangle"""
        return f"[Rectangle] ({self.id}) " \
            + f"{self.x}/{self.y} - {self.width}/{self.height}"

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute
            id - width - height - x - y
        """
        if len(args) == 0:
            for k, v in kwargs.items():
                # if hasattr(self, k):
                setattr(self, k, v)
        else:
            try:
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]
                self.x = args[3]
                self.y = args[4]
            except IndexError:
                pass

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle"""
        return {'id': self.id,
                'width': self.width,
                'height': self.height,
                'x': self.x,
                'y': self.y}
