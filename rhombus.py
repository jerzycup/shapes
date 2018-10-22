from parallelogram import Parallelogram

class Rhombus(Parallelogram):
    '''
    Rhombus

    parameters:
    a - length of side
    fi - angle between side and base
    '''

    def __init__(self, a, fi):
        super().__init__(a, a, fi)