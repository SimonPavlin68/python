import sympy as sym

x = sym.symbols('x')

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