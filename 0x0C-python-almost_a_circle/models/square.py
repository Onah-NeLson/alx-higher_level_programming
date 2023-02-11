#!/usr/bin/python3
"""
Module based on class Rectangle
Contains a class called Square
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """This class inherits from Rectangle and defines a square object

    Attributes:
        size (int): The width of the square
        x (int): The horizontal (x) padding of the square
        y (int): The vertical (y) padding of the square
        id (int): The identification of the object
    """
    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a square object

        Args:
            size (int): The width of the square
            x (int): The horizontal (x) padding of the square
            y (int): The vertical (y) padding of the square
            id (int): The identification of the square object
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Overrides the default behaviour of the __str__ method."""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    # width attribute getter and setter
    @property
    def size(self):
        """Retrieves the value of the size"""
        return (self.width)

    @size.setter
    def size(self, value):
        """Sets the necessary attributes for the square object.

        Args:
            size (int): the size of the square
            Raises:
                TypeError: if size is not given as an integer
                ValueError: if size is less than 0.
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        ""assigns an argument to each attribute
        Args:
            args(list): attributes to be modified[id, size, x, y].
            kwargs(dict): attributes to be modified.
        """
        if args is not None and len(args) != 0:
            arlist = ["id", "size", "x", "y"]
                for arl in range(len(args)):
                    if arl == 0:
                        super().update(args[arl])
                    elif arl < len(arlist):
                        setattr(self, arlist[arl], args[arl])
                else:
                    for key, value in kwargs.items():
                        if (key == 'id'):
                            super().update(value)
                        else:
                            setattr(self, key, value)

    def to_dictionary(self):
        """returns the dictionary
        representation of a Square
        """

        dico = {'id': self.id, 'x': self.x, 'size': self.width, 'y': self.y}
        return dico
