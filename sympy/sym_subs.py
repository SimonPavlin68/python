import sympy as sym

x, y = sym.symbols('x y')

f = x**2 + y

print(f.subs({x: 5, y: 7}))

sym.plot(f.subs(y, 7), (x, -3, 3));

sym.plot(f.subs({y: 7}))