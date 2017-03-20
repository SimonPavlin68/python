import numpy as np
import sympy as sym
from scipy import optimize

A = 1.1 # m
l = 1.4 # m
n = 1000 # /
r = 1.1 # m


a = np.linspace(0, 2*np.pi, n)
#alpha = sym.symbols('alpha')
#f = r*sym.cos(alpha) + sym.sqrt(l**2 - (r*sym.sin(alpha))**2)

#f2 = sym.diff(f, alpha)
#print(f2)
#f3 = sym.diff(f2, alpha)
#print(f3)

def func1(a):
    return -1.1 * sym.cos(a) + 1.21 * sym.sin(a) ** 2 / sym.sqrt(-1.21 * sym.sin(a) ** 2 + 1.96) - 1.21 * sym.cos(a) ** 2 / sym.sqrt(
        -1.21 * sym.sin(a) ** 2 + 1.96) - 1.4641 * sym.sin(a) ** 2 * sym.cos(a) ** 2 / (-1.21 * sym.sin(
        a) ** 2 + 1.96) ** (3 / 2)

def func(a):
    return r * sym.cos(a) + sym.sqrt(l**2 - (r * sym.sin(a))**2) - A

print('kurc1')
rez5 = optimize.newton(func1, 0.1)
print(rez5)
print('kurc2')


