#!/usr/bin/python3
"""
Module that contains the Class Base
"""
import json
import csv
import turtle


class Base:
    """ Base class of all other classes in this project"""
    __nb_objects = 0

    def __init__(self, id=None):
        """ Class constructor """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries.

        Args:
            list_dictionaries (list): a list of dictionnary
        """
    if list_dictionaries is None or len(list_dictionaries) == 0:
        return "[]"
    return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file.

        Args:
            list_objs (list): list of instances who inherits of Base
        """
        filename = type(list_objs[0]).__name__ + '.json'
        with open(filename, 'w') as f:
            if list_objs is None:
                json.dump([], f)
            elif type(list_objs[0]).__name__ == 'Rectangle':
                new_dict = [item.to_dictionary() for item in list_objs]
                json_string = cls.to_json_string(new_dict)
                json.dump(json_string, f)

    @staticmethod
    def from_json_string(json_string):
        """eturns the list of the JSON string representation json_string.

        Args:
            json_string (string) : string representing a list of dictionaries
        """
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set
        Args:
           **dictionary (dictionary): can be thought of as a double pointer
           to a dictionary
        """
        if cls.__name__ == "Rectangle":
            new = cls(1, 1)
        else:
            new = cls(1)
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances."""
        try:
            with open(cls.__name__ + ".json", 'r') as f:
                json_file = Base.from_json_string(f.read())
            return [cls.create(**dct)
                    for dct in json_file]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes the CSV string representation of list_objs to a file.

        Args:
            list_objs (list): a list of objects.
        """
        fields = []
        with open(cls.__name__ + ".csv", 'w') as f:
            if list_objs is None or len(list_objs) <= 0:
                f.write('[]')
            else:
                if cls.__name__ == "Rectangle":
                    fields = ['id', 'width', 'height', 'x', 'y']
            elif cls.__name__ == "Square":
                fields = ['id', 'size', 'x', 'y']
            writer = csv.DictWriter(f, fieldnames=fields)
            for obj in list_objs:
                writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """
        Deserializes the CSV string representation
        of list_objs from a file.
        """
        fields = []
        try:
            with open(cls.__name__ + ".csv", 'r') as f:
                if cls.__name__ == "Rectangle":
                    fields = ['id', 'width', 'height', 'x', 'y']
                elif cls.__name__ == "Square":
                    fields = ['id', 'size', 'x', 'y']
            reader = csv.DictReader(f, fieldnames=fields)
            dcts = [dict([k, int(v)] for k, v in el.items())
                    for el in reader]
            return [cls.create(**dct) for dct in dcts]

        except IOError:
            return []

    def draw(list_rectangles, list_squares):
        """Opens a window and draws all the Rectangles and Squares.

        Args:
            list_rectangles (list): a list of rectangle instances.
            list_squares (list): a list of square instances.
        """
        t = turtle.Turtle()
        t.screen.bgcolor('#000000')
        t.shape('turtle')
        t.color('#ffffff')
        t.penup()
        t.goto(-200, 200)
        for rect in list_rectangles:
            t.goto(t.xcor() + (rect.width + 20), t.ycor() - (rect.height + 20))
            t.up()
            t.down()
            for i in range(2):
                t.forward(rect.width)
                t.left(90)
                t.forward(rect.height)
                t.left(90)
                t.penup()
            t.goto(-200, -20)
        for squ in list_squares:
            t.goto(t.xcor() + (squ.width + 20), t.ycor() - (squ.height + 20))
            t.up()
            t.down()
            for i in range(2):
                t.forward(squ.width)
                t.left(90)
                t.forward(squ.height)
                t.left(90)
                t.penup()
        t.Screen().exitonclick()
