# coding: utf8
import numpy as np
import circle
import rectangles
import triangle
import quadrangle
import parallelogram
import trapezoid
import rhombus

shape = circle.Circle(3)
#shape = rectangles.Rectangle(2, 3)
#shape = triangle.Triangle(np.array([2, 3]), np.array([5, 2]))
#shape = quadrangle.Quadrangle(np.array([1, 2]), np.array([5, -3]), np.array([0, 3]))
#shape = parallelogram.Parallelogram(1, 2, 30)
#shape = trapezoid.Trapezoid(2, 1, 60, 30)
#shape = rhombus.Rhombus(3, 40)
#shape = rectangles.Square(1)

print(shape.draw())
