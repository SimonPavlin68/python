import sympy as sym

x, t = sym.symbols('x t')

f1 = sym.sin(x)
f2 = sym.diff(f1, x)

p1 = sym.plot(f1, (x, -2*sym.pi, 2*sym.pi), show=False, line_color='b')
p2 = sym.plot(f2, (x, -2*sym.pi, 2*sym.pi), show=False, line_color='r')
p1.extend(p2)
p1.show()

f3 = 3*x**3 - 2*x**2 + x +7
f4 = sym.diff(f3, x, x)

p3 = sym.plot(f3, (x, -2, 2), show=False, line_color='b')
p4 = sym.plot(f4, (x, -2, 2), show=False, line_color='r')
p3.extend(p4)
p3.show()

import numpy as np
g = 9.81    # gravitacijski pospešek
v0 = 10     # začetna hitrost
alpha = 35  # kot
h = 3       # začetna višina
f5 = h + v0*t*sym.sin(np.deg2rad(alpha)) - (g*t**2)/2
f6 = sym.diff(f5, t)
p5 = sym.plot(f5, (t, 0, 2), show=False, line_color='b')
p6 = sym.plot(f6, (t, 0, 2), show=False, line_color='r')
p5.extend(p6)
p5.show()

from scipy import optimize
root = optimize.newton(f6, 1.5)
print('optimize.newton', root)