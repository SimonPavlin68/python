import sympy as sym

sym.init_printing()

x, y, k = sym.symbols('x y k')

f = (x**y + sym.pi)**2

z = f.subs({x: 1.5, y: 2, sym.pi: sym.N(sym.pi,15)})

print(z)

#sym.plot(f.subs(x, 1.1), (y, 0, 10), xlabel='y spr');

sym.plot(x**2, 10*x)
