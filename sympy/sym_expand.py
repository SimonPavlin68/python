import sympy as sym

sym.init_printing()

x, y, k = sym.symbols('x y k')

f = (x+1)*(x+2)*(x+3)

ex = sym.expand(f)
print(ex)

#print(ex.coeff(x))

a, b = sym.symbols('a b')
print(sym.expand(sym.sin(a+b), trig=True))

f = (x+1)*(x+1)*(x+3)
print(sym.simplify(f))