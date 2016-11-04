import sympy as sym

x, y = sym.symbols('x, y')
sym.plotting.plot3d(x*y, (x, -5, 5), (y, -5, 5))