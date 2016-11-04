import sympy as sym

x = sym.symbols('x')
#en = sym.Eq(sym.sin(x**2), 0.5)
#en = sym.Eq(x**2, 4)
#print(sym.solve(en, x))

#sym.plot(sym.sin(x**2), 0.5, (x, -sym.pi, sym.pi))
sym.plot(x**3 - x**2 + x, (x, -3, 3))

#en = sym.Eq(x+2, 7)

#en = sym.Eq(x**2 + y, 7)
#print(sym.solve(en, [x, y]))

#a, b, c = sym.symbols('a b c')
#s = sym.solve(a*x**2 + b*x + c, x)


#s = sym.solve([x+y-1, x-y-1], [x,y])
#print(s)