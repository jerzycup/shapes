from shape import Shape

class Quadrangle(Shape):
    '''
    Any quadrangle

    Parameters
    a, b, c - 2 dimensional vectors
    '''

    a = None
    b = None
    c = None

    def __str__(self):
        self.a = a
        self.b = b
        self.c = c
        self.d = (self.a - self.c) - self.b
        if a.shape != (2,) or b.shape != (2,) or c.shape != (2,):
            raise ValueError('paramters have to be vectors')