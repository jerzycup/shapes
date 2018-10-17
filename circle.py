from shape import Shape
import numpy as np

class Circle(Shape):
    '''
    circle shape

    Parameters:
    r - radius, int
    '''

    r = None

    def __init__(self, r):
        self.r = r
        if self.r < 0:
            raise ValueError('Radius cannot be smaller than 0')

    def __str__(self):
        return self.r

    def area(self):
        return np.pi * self.r**2

    def perimeter(self):
        return 2 * np.pi * self.r