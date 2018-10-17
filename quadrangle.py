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

    def __str__(self, a, b, c):
        super().__init__()
        self.a = a
        self.b = b
        self.c = c
        self.d = (self.a - self.c) - self.b
        if a.shape != (2,) or b.shape != (2,) or c.shape != (2,):
            raise ValueError('Paramters have to be vectors')

    def __str__(self):
        return 'Vectors: {}, {}, {}, {}'.format_map(self.a, self.b, self.c, self.d)

    def area(self):
        return 0.5 * abs(self.a[0] * self.b[1] - self.a[1] * self.b[0]) + 0.5 * abs((self.c[0] * self.d[1] - self.c[1] * self.d[0]))

    def perimeter(self):
        return np.linalg.norm(self.a) + np.linalg.norm(self.b) + np.linalg.norm(self.c) + np.linalg.norm(self.d)
