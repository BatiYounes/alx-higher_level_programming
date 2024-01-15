#!/usr/bin/python3
"""Base class"""
import json
import csv
import turtle


class Base:
    """Base class (blueprint) for objrcts.
    private class attribute: __nb_objects = 0.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """init Base class.

        Args:
            id: to avoid duplicating the same code.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries.

        Args:
            list_dictionaries: list of dictionaries.
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file.

        Args:
            list_objs: list of instances who inherits of Base.
        """
        file_name = cls.__name__ + ".json"
        with open(file_name, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dictionaries = [obj.to_dictionary() for obj in list_objs]
                jsonfile.write(Base.to_json_string(list_dictionaries))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string.

        Args:
            json_string: string representing a list of dictionaries.
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set.

        Args:
            **dictionary: double pointer to a dictionary.
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                dummy_instance = cls(3, 7)
            else:
                dummy_instance = cls(3)
            dummy_instance.update(**dictionary)
            return dummy_instance

    @classmethod
    def load_from_file(cls):
        """returns a list of instances."""
        file_name = str(cls.__name__) + ".json"
        try:
            with open(file_name, "r") as jsonfile:
                list_dictionaries = Base.from_json_string(jsonfile.read())
                return [cls.create(**dicti) for dicti in list_dictionaries]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """serializes list of objects to a file.

        Args:
            list_objs: list of instances who inherits of Base.
        """
        file_name = cls.__name__ + ".csv"

        with open(file_name, "w", newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fields = ["id", "width", "height", "x", "y"]
                else:
                    fields = ["id", "size", "x", "y"]

                writer = csv.DictWriter(csvfile, fieldnames=fields)

                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """deserializes list of objects from a file."""
        file_name = cls.__name__ + ".csv"

        try:
            with open(file_name, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fields = ["id", "width", "height", "x", "y"]
                else:
                    fields = ["id", "size", "x", "y"]
                lst_dct = csv.DictReader(csvfile, fieldnames=fields)
                lst_dct = [dict([_key, int(_val)] for _key, _val in d.items())
                           for d in lst_dct]
                return [cls.create(**d) for d in lst_dct]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """opens a window and draws all the Rectangles and Squares.

        Args:
            list_rectangles: list of Rectangle objects to draw.
            list_squares: list of Square objects to draw.
        """
        draw_object = turtle.Turtle()
        draw_object.screen.bgcolor("#FDFEFE")
        draw_object.pensize(7)
        draw_object.shape("circle")

        draw_object.color("#196F3D")
        for rectangle in list_rectangles:
            draw_object.showturtle()
            draw_object.up()
            draw_object.goto(rectangle.x, rectangle.y)
            draw_object.down()
            for i in range(2):
                draw_object.forward(rectangle.width)
                draw_object.left(90)
                draw_object.forward(rectangle.height)
                draw_object.left(90)
            draw_object.hideturtle()

        draw_object.color("#D4AC0D")
        for square in list_squares:
            draw_object.showturtle()
            draw_object.up()
            draw_object.goto(square.x, square.y)
            draw_object.down()
            for i in range(2):
                draw_object.forward(square.width)
                draw_object.left(90)
                draw_object.forward(square.height)
                draw_object.left(90)
            draw_object.hideturtle()

        turtle.exitonclick()
