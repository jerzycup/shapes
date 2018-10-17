from shape import Shape

class Triangle(Shape):
    """
    triangle shape
    """

    a = None
    b = None

    def __init__(self, a, b):
        self.a = a
        self.b = b
        if isinstance(a, list) == False or isinstance(b ,list) == False:
            raise ValueError('it have to be vectors')