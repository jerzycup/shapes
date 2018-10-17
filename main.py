# coding: utf8
import numpy as np
import rectangles
import triangle
'''
square2 = rectangles.Square(2)

print(square2.summary())

print(isinstance(square2, rectangles.Rectangle))
'''
vec1 = np.array([0, 3])
vec2 = np.array([4, 0])

tr1 = triangle.Triangle(vec1, vec2)

print(tr1.summary())