import sympy as sym

x, y, z, h = sym.symbols('x y z h')
# 1
print(sym.limit(sym.sin(x)/x, x, 0))

# 2
f = sym.sin(x*y) + sym.cos(y*z)
print(sym.diff(f, x))
print(sym.limit((f.subs(x, x+h) - f)/h, h, 0))