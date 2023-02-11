#!/usr/bin/python3
"""
Module that contain a class Rectangle
Class that inherit from Base
"""
from models.base import Base


class Rectangle(Base):
    """Class that defines a rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Class constructor"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def __str__(self):
        """Overrides the default behaviour of the __str__ method."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height)

    # width attribute getter and setter
    @property
    def width(self):
        """Retrieves the value of the width"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """Sets the necessary attributes for the Rectangle object.
        Args:
            width (int): the width of the square.
        Raises:
            TypeError: if width is not given as an integer.
            ValueError: if width is less than 0.
        """
        if (type(value) != int):
            raise TypeError("width must be an integer")
        elif (value < 0):
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    # height attribute getter and setter.
    @property
    def height(self):
        """Retrieves the value of the height"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """Sets the necessary attributes for the Rectangle object.
        Args:
            height (int): the height of the square.
        Raises:
             TypeError: if width is not given as an integer.
             ValueError: if height is less than 0.
        """
    if (type(value) != int):
        raise TypeError("height must be an integer")
    elif (value < 0):
        raise ValueError("height must be >= 0")
    else:
        self.__height = value

    # x attribute getter and setter.
    @property
    def x(self):
        """Retrieves the value of x"""
        return (self.__x)

    @x.setter
    def x(self, value):
        ""Sets the necessary attributes for the Rectangle object.
        Args:
            x(int): the width of the square.
        Raises:
            TypeError: if width is not given as an integer.
            ValueError: if width is less than 0.
        """
        if (type(value) != int):
            raise TypeError("x must be an integer")
        elif (value < 0):
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    # y attribute getter and setter.
    @property
    def y(self):
        """Retrieves the value of x"""
            return (self.__y)

    @y.setter
    def y(self, value):
        """Sets the necessary attributes for the Rectangle object.
        Args:
            x(int): the width of the square.
        Raises:
            TypeError: if width is not given as an integer.
            ValueError: if width is less than 0.
        """
        if (type(value) != int):
            raise TypeError("y must be an integer")
        elif (value < 0):
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    # Methods
    def area(self):
        """Retrieves the area of the Rectangle"""
        return (self.__width * self.__height)

    def display(self):


        """  prints in stdout the Rectangle instance with the character'#'
        """
        print('\n' * self.y, end='')
        for height in range(self.height):
            print(' ' * self.x + '#' * self.width)

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute
        Args:
            args(list): attributes to be modified[id, width, height, x, y].
            kwargs(dict): attributes to be modified.
        """
        if (args is not None) and (len(args) != 0):
            arlist = ["id", "width", "height", "x", "y"]
            for arl in range(len(args)):
                if arl == 0:
                    super().__init__(args[arl])
                else:
                    setattr(self, arlist[arl], args[arl])
        else:
            for key, value in kwargs.items():
                if (key == 'id'):
                    super().__init__(value)
                else:
                    setattr(self, key, value)

    def to_dictionary(self):
        ""returns the dictionary representation of a Rectangle"""
        dico = {'x': self.__x, 'y': self.__y,
                'id': self.id, 'height': self.height, 'width': self.width}
        return dico
