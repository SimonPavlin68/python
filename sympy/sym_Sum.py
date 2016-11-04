import sympy as sym

x, n = sym.symbols('x n')

f = 4*((-1)**n)/(2*n+1)

print(sym.Sum(f, (n, 0, 100)))
print(sym.Sum(f, (n, 0, 100)).evalf(n=10))

f = sym.Sum(1/x**n, (n, 1, 10))

print('f', f)

print('f.doit', f.doit())

print('f.subs', f.subs({x: 2}).evalf())