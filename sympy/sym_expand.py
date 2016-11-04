import sympy as sym

sym.init_printing()

x, y, k = sym.symbols('x y k')
f1 = (x+1)*(x+2)*(x+3)
f1

ex = sym.expand(f1)
print(ex)

a, b = sym.symbols('a b')
f2 = sym.sin(a+b)
print(f2)
print(sym.expand(f2, trig=True))

f3 = (x+1)*(x+1)*(x+3)
print(f3)
print(sym.simplify(f3))