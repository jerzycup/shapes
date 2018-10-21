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
        rad = 2 * np.pi / 360
        self.a = a
        self.b = b
        self.fi = fi * rad
        if fi >= 180:
            raise ValueError('angle cannot be bigger than 180°')
        if a <= 0 or b <= 0:
            raise ValueError('lengths of sides and bases have to be positive')
