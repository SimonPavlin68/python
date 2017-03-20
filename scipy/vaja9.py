import numpy as np
import sympy as sym
import matplotlib.pyplot as plt

A = 1.1 # m
l = 1.4 # m
n = 1000 # /
r = 1.1 # m

# odg 2
alpha = np.linspace(0, 2*np.pi, n)
x_alpha = r * np.cos(alpha) + np.sqrt(l**2 - (r * np.sin(alpha))**2)
print(x_alpha)
plt.plot(alpha, x_alpha)
plt.axhline(A, color='r')
plt.show()

from scipy import optimize

# odg 4
def func(alpha):
    return r * np.cos(alpha) + np.sqrt(l ** 2 - (r * np.sin(alpha)) ** 2) - A

rez4 = optimize.newton(func, 1)
print('optimize.newton', rez4)

rez4a = optimize.newton(func, 5)
print('optimize.newton', rez4a)

#x_alpha = r * np.cos(alpha) + np.sqrt(l**2 - (r * np.sin(alpha))**2)
plt.plot(alpha, func(alpha))
plt.axhline(A, color='r')
plt.axhline(0, color='k')
plt.axvline(rez4, color='k')
plt.axvline(rez4a, color='k')
#plt.show()

# odg 3 - odvod
alpha = sym.symbols('alpha')
f = r*sym.cos(alpha) + sym.sqrt(l**2 - (r*sym.sin(alpha))**2)

f2 = sym.diff(f, alpha)
print(f2)
f3 = sym.diff(f2, alpha)

p1 = sym.plot(f, (alpha, 0, 2*sym.pi), show=False, line_color='r')
p2 = sym.plot(f2, (alpha, 0, 2*sym.pi), show=False, line_color='g')
p3 = sym.plot(f3, (alpha, 0, 2*sym.pi), show=False, line_color='b')
p1.extend(p2)
p1.extend(p3)
p1.show()

rez5 = optimize.newton(f3, 1)
print('optimize.newton', rez5)

