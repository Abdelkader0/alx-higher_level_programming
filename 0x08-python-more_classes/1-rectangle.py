#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

        @property
        def width(self):
            """Get/set the width"""
            return self.__width

        @width.setter
        def width(self, value):
            if not isinstance(value, int):
                raise TypeError("width must be integer")
            if value < 0:
                raise TypeError("width must be >= 0")
            self.__width = value

        @property
        def height(self):
            """Get/set the Height"""
            return self.__height

        @height.setter
        def height(self, value):
            if not isinstance(value, int):
                raise TypeError("height must be an integer")
            if value < 0:
                raise TypeError("value must be >= 0")
            self.__height
