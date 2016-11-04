import sympy as sym

sym.init_printing()

x, y, z = sym.symbols('x y z')
f1 = sym.sin(x)**2
f1

f2 = sym.Integral(sym.sqrt(1/x),x)
f2

