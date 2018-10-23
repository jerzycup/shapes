from shape import Shape
import numpy as np
from parallelogram import Parallelogram

class Trapezoid(Shape):
    '''
    Trapezoid

    Parameters:
    a, b - length of bases
    fi, theta - angles between a and sides given in °
    '''

    a = None
    b = None
    fi = None
    theta = None

    def __init__(self, a, b, fi, theta):
        rad = 2 * np.pi / 360
        self.a = a
        self.b = b
        self.fi = fi * rad
        self.theta = theta * rad
        self.h = abs(a - b)/(1/np.tan(fi) + 1/np.tan(theta))
        if fi >= 180 or theta >= 180:
            raise ValueError('angles cannot be bigger than 180°')
        if a <= 0 or b <= 0:
            raise ValueError('lengths of bases have to be positive')
        if fi + theta == 180:
            raise Exception('For the case when sum of both angles is equal 180 there are infinitely many possible '
                            'trapezoids. If you really want to calculate for this case use class "Parallelogram"')

    def __str__(self):
        return 'Bases: {}, {}, Angles: {}, {}, Height: {}'.format(self.a, self.b, self.fi, self.theta, self.h)

    def area(self):
        return 0.5 * (self.a + self.b) * self.h

    def perimeter(self):
        return self.a + self.b + self.h/np.sin(self.fi) + self.h/np.sin(self.theta)

    def apex(self):
        x0 = np.array([0, 0])
        x1 = np.array([self.a, 0])
        x2 = np.array([self.a - self.h/np.tan(self.fi), self.h])
        x3 = np.array([x2[0] - self.b, self.h])

        x = np.array([x0, x1, x2, x3, x0])

        print(x)

        return x
