#!/usr/bin/python3
"""Defines a base geometry class BaseGeometry."""


class BaseGeometry:
    """Depict or describe the fundamental geometry."""

    def area(self):
        """raises an exception when called"""
        raise Exception("area() is not implemented")
