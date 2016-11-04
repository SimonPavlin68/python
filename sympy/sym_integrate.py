import sympy as sym

x = sym.symbols('x')

f1 = sym.sin(x)
f2 = sym.integrate(f1, x)

p1 = sym.plot(f1, (x, -2*sym.pi, 2*sym.pi), show=False, line_color='b')
p2 = sym.plot(f2, (x, -2*sym.pi, 2*sym.pi), show=False, line_color='r')
p1.extend(p2)
p1.show()

f3 = 3*x**3 - 2*x**2 + x +7
f4 = sym.integrate(f3, x)

p3 = sym.plot(f3, (x, -2, 2), show=False, line_color='b')
p4 = sym.plot(f4, (x, -2, 2), show=False, line_color='r')
p3.extend(p4)
p3.show()

#print(sym.integrate(sym.exp(-x**2), (x, -sym.oo, sym.oo)))
#print(sym.integrate(sym.exp(-x**2), (x, 0, 1)).evalf(n=10))

r, dfi = sym.symbols('r dfi')
dP = r/sym.pi*r*dfi/2

P = sym.integrate(dP, (dfi, 0, 2*sym.pi))
print('P = {0}'.format(P))