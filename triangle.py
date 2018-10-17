from shape import Shape
import numpy as np

class Triangle(Shape):
    """
    triangle shape
    """

    a = None
    b = None

    def __init__(self, a, b):
        self.a = a
        self.b = b
        if a.shape != (2,)  or b.shape != (2,):
            raise ValueError('it has to be 2 dimensional vectors')

