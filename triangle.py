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
            raise ValueError('Parameters have to be 2 dimensional vectors')
        if a[0]/np.linalg.norm(a) == b[0]/np.linalg.norm(b) and a[1]/np.linalg.norm(a) == b[1]/np.linalg.norm(b):
            raise ValueError('Vectors have to be in different directions')

    def __str__(self):
        return 'Vectors: {}, and {}'.format(self.a, self.b)

    @property
    def area(self):
        return 0.5 * abs(self.a[0] * self.b[1] - self.a[1] * self.b[0])

    @property
    def perimeter(self):
        return np.linalg.norm(self.a) + np.linalg.norm(self.b) + np.linalg.norm(np.add(self.a, -self.b))

    def apex(self):
        x = np.array([np.array([0, 0]), self.a, self.b, np.array([0, 0])])
        return x
