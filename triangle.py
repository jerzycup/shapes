from shape import Shape
import numpy as np

class Triangle(Shape):
    """
    triangle shape

    Parameters:
    a, b - 2 dimensional vectors
    """

    a = None
    b = None

    def __init__(self, a, b):
        self.a = a
        self.b = b
        if a.shape != (2,)  or b.shape != (2,):
            raise ValueError('it has to be 2 dimensional vectors')

    def __str__(self):
        return 'Vectors: {}, and {}'.format(self.a, self.b)

    def area(self):
        return 0.5 * abs(self.a[0] * self.b[1] - self.a[1] * self.b[0])

    def perimeter(self):
        return np.linalg.norm(self.a) + np.linalg.norm(self.b) + np.linalg.norm(np.add(self.a, -self.b))