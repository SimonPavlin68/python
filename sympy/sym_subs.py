import sympy as sym

x, y = sym.symbols('x y')

f = x**2

sym.plot(f.subs(y, 0, 5))