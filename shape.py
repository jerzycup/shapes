# coding: utf8
from matplotlib import pyplot as plt


class Shape(object):
    """
    Base class for all shapes.
    """

    def area(self):
        """
        Abstract method returning area of a shape.
        """

    def perimeter(self):
        """
        Abstract method returning shape perimeter.
        """

    def summary(self):
        """
        Return summary of a shape.
        """
        return {
            'area': self.area(),
            'perimeter': self.perimeter()
        }

    def apex(self):
        '''
        Abstract method of finding apexes
        '''

    def draw(self):
        '''
        Returns a plot
        '''
        data = self.apex()
        x, y = data.T
        plt.plot(x, y, '-')
        plt.axis('scaled')
        plt.show()


