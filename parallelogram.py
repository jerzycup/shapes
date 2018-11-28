from shape import Shape
import numpy as np

class Parallelogram(Shape):
    '''
    Parallelogram

    Parameters:
    a - length of bases
    b - length of sides
    fi - angle between base and side given in °
    '''

    a = None
    b = None
    fi = None

    def __init__(self, a, b, fi):
        super().__init__()
        rad = 2 * np.pi / 360
        self.a = a
        self.b = b
        self.fi = fi * rad
        if fi >= 180:
            raise ValueError('angle cannot be bigger than 180°')
        if a <= 0 or b <= 0:
            raise ValueError('lengths of sides and bases have to be positive')

    @property
    def area(self):
        return self.a * self.b * np.sin(self.fi)

    @property
    def perimeter(self):
        return 2 * self.a + 2 * self.b

    def apex(self):
        x0 = np.array([0,0])
        x1 = np.array([self.a, 0])
        x2 = np.array([self.a + self.b * np.cos(self.fi), self.b * np.sin(self.fi)])
        x3 = np.array([x2[0] - self.a, x2[1]])

        x = np.array([x0, x1, x2, x3, x0])

        return x
