from shape import Shape
import numpy as np

class Quadrangle(Shape):
    '''
    Any convex quadrangle

    Parameters
    a, b, c - 2 dimensional vectors
    '''

    a = None
    b = None
    c = None

    def __init__(self, a, b, c):
        super().__init__()

        self.a = a
        self.b = b
        self.c = c
        self.d = (self.a - self.c) - self.b
        if a.shape != (2,) or b.shape != (2,) or c.shape != (2,):
            raise ValueError('Parameters have to be vectors')
        if (a[0]/np.linalg.norm(a) == b[0]/np.linalg.norm(b) and a[1]/np.linalg.norm(a) == b[1]/np.linalg.norm(b)) or\
            (c[0]/np.linalg.norm(c) == b[0]/np.linalg.norm(b) and c[1]/np.linalg.norm(c) == b[1]/np.linalg.norm(b)) or\
            (a[0]/np.linalg.norm(a) == c[0]/np.linalg.norm(c) and a[1]/np.linalg.norm(a) == c[1]/np.linalg.norm(c)):
            raise ValueError('Vectors have to be in different directions')

    def __str__(self):
        return 'Vectors: {}, {}, {}, {}'.format_map(self.a, self.b, self.c, self.d)

    def area(self):
        return 0.5 * abs(self.a[0] * self.b[1] - self.a[1] * self.b[0]) + 0.5 * abs((self.c[0] * self.d[1] - self.c[1] * self.d[0]))

    def perimeter(self):
        return np.linalg.norm(self.a) + np.linalg.norm(self.b) + np.linalg.norm(self.c) + np.linalg.norm(self.d)

    def apex(self):
        f = [self.a, self.b, self.c, self.d]

        xpos = []
        xneg = []
        x0 = []

        for i in range(3):
            if f[i][0] > 0:
                xpos.append(f[i])
            if f[i][0] < 0:
                xneg.append(f[i])
            if f[i][0] == 0:
                x0.append(f[i])

        f = []
        for j in range(len(x0)):
            if x0[j][1] < 0:
                f.append(x0[j])

        def tan(x):
            return x[1]/x[0]

        xpos.sort(key=tan)
        xneg.sort(key=tan)

        for k in range(len(xpos)):
            f.append(xpos[k])

        for l in range(len(x0)):
            if x0[l][1] > 0:
                f.append(x0[l])

        for m in range(len(xneg)):
            f.append(xneg[m])

        x = np.array([np.array([0, 0]), f[0], f[0] + f[1], f[0] + f[1] + f[2], np.array([0, 0])])
        return x
