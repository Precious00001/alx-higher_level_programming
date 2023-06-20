#!/usr/bin/python3
"""
base model class
"""
import json
import csv


class Base:
    """
    Base model
    Attributes:
        __nb_object : private class atribute
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Init
        Attributes:
            id (): id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
            Return A JSON STRING a representation list_dict..
        """
        if not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
            Save Dict To Json
        """
        p = []
        with open(cls.__name__ + ".json", "w", encoding="utf-8") as f:
            if list_objs:
                for obj in list_objs:
                    p.append(obj.to_dictionary())
            f.write(cls.to_json_string(p))

    @staticmethod
    def from_json_string(json_string):
        """
            Return the deserialization of a JSON string.

        Args:
            json_string (str): A JSON str representation of a list of dicts.
        Returns:
            If json_string is None or empty - an empty list.
            Otherwise - the Python list represented by json_string.
        """
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
            Return a class instantied from a dictionary of attributes.

        Args:
            **dictionary (dict): Key/value pairs of attributes to initialize.
        """
        if cls.__name__ == 'Rectangle':
            q = cls(1, 1)
        if cls.__name__ == 'Square':
            q = cls(1)
        q.update(**dictionary)
        return q

    @classmethod
    def load_from_file(cls):
        """
            Return a list of classes instantiated from a file of JSON strings.

        Reads from `<cls.__name__>.json`.

        Returns:
            If the file does not exist - an empty list.
            Otherwise - a list of instantiated classes.
        """
        try:
            with open(cls.__name__ + ".json", "r") as f:
                return [cls.create(**dictionary) for
                        dictionary in cls.from_json_string(f.read())]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Write the CSV serialization of a list of objects to a file."""
        e = []
        with open(cls.__name__ + ".csv", "w", encoding="utf-8") as f:
            if list_objs:
                for obj in list_objs:
                    if cls.__name__ == 'Rectangle':
                        e.append([
                            obj.id, obj.width, obj.height, obj.x, obj.y])
                    if cls.__name__ == 'Square':
                        e.append([obj.id, obj.size, obj.x, obj.y])
            writer = csv.writer(f)
            for row in e:
                writer.writerow(row)

    @classmethod
    def load_from_file_csv(cls):
        """Return a list of classes instantiated from a CSV file.

        Reads from `<cls.__name__>.csv`.

         Returns:
            If the file does not exist - an empty list.
            Otherwise - a list of instantiated classes."""
        try:
            with open(cls.__name__ + ".csv", "r") as f:
                e = []
                reader = csv.DictReader(f)
                for row in reader:
                    for key, val in row.items():
                        row[key] = int(val)
                e.append(row)
                return [cls.create(**item) for item in e]
        except FileNotFoundError:
            return []
