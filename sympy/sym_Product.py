import sympy as sym

x, n = sym.symbols('x n')

f = sym.Product(1/n, (n, 1, 10))

print('f', f)

print('f.doit', f.doit())

print('f.subs', f.subs({x: 1}).evalf())