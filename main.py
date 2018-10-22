# coding: utf8
import numpy as np
import rectangles
import triangle
import quadrangle
import circle
import parallelogram
import trapezoid
import rhombus

vec1 = np.array([2, 2])
vec2 = np.array([-1, 1])

shape = triangle.Triangle(vec1, vec2)


print(shape.draw())
