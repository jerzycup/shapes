from shape import Shape
import numpy as np

class trapezoid(shape):
    '''
    Trapezoid

    Paramteres
    a, b - length of bases
    fi, theta - angles between a and sides given in °
    '''

    a = None
    b = None
    fi = None
    theta = None

    def __init__(self, a, b, fi, theta):
        super().__init__()
        self.a = a
        self.b = b
        self.fi = fi
        self.theta = theta
        self.h = bs(b - a)/(1/np.tan(fi) + 1/np.tan(theta))
        if fi >= 180 or theta >= 180:
            raise ValueError('angles cannot be bigger than 180°')

    def __str__(self):
        return 'Bases: {}, {}, Angles: {}, {}, Height: {}'.format(self.a, self.b, self.fi, self.theta, self.h)

    def area(self):
        return 0.5 * (self.a + self.b) * self.h

    def perimeter(self):
        return self.a + self.b + self.h/np.sin(self.fi) + self.h/np.sin(self.theta)
