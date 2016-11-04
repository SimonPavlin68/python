import sympy as sym

x = sym.symbols('x')

f = x**2

sym.plot(f.subs(0, 5))