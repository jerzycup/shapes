# coding: utf8
from parallelogram import Parallelogram


class Rectangle(Parallelogram):
    """
    Rectangular shape.
    """

    a = None
    b = None

    def __init__(self, a, b):
        super().__init__(a, b, 90)

class Square(Parallelogram):
    """
    Square shape as a specific rectangle.
    """

    def __init__(self, a):
        super().__init__(a, a, 90)
