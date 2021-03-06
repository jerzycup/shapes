from shape import Shape
import numpy as np
from matplotlib import pyplot as plt

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

    @property
    def area(self):
        return np.pi * self.r**2

    @property
    def perimeter(self):
        return 2 * np.pi * self.r

    def apex(self):
        raise Exception('There are no apexes in circle')

    def draw(self):
        circle = plt.Circle((0, 0), self.r, fill=False)
        fig, ax = plt.subplots()
        ax.add_artist(circle)
        ax.axis('scaled')
        ax.axis([-1.1 * self.r, 1.1 * self.r, -1.1 * self.r, 1.1 * self.r])

        plt.show()
