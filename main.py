# coding: utf8
import numpy as np
import rectangles
import triangle
import quadrangle

square2 = rectangles.Square(2)

print(square2)

print(isinstance(square2, rectangles.Rectangle))

vec1 = np.array([0, 2])
vec2 = np.array([2, 0])

tr1 = triangle.Triangle(vec1, vec2)

print(tr1.summary())

vec3 = np.array([0, 2])

qu1 = quadrangle.Quadrangle(vec1, vec2, vec3)

print(qu1.summary())
