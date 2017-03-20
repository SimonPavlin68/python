import numpy as np
import sympy as sym
import matplotlib.pyplot as plt
import math

q = 5 #[KN/m]
a = 0.5 #[m]
F = 2 #KN
fi = 60
firad = (fi * np.pi)/180
Fx = sym.cos(firad) * F
Fy = sym.sin(firad) * F
Q = q*4*a


Ax, Ay, By = sym.symbols('Ax, Ay, By')

A = sym.Matrix([[1, 0, 0], [0, 0, (-7*a)], [0, (-7*a), 0]])
x = sym.Matrix([[Ax], [Ay], [By]])
b = sym.Matrix([[Fx], [-(Q+Fy*5*a)], [-(Q*5*a+Fy*2*a)]])


eq = sym.Eq(A*x, b)

print(sym.solve(eq, [Ax, Ay, By]))
