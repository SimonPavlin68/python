import sympy as sym
import numpy as np
import matplotlib.pyplot as plt

g = 9.81
v0 = 50
l = 50
alpha = np.deg2rad(15)

print('x', l*sym.cos(alpha), 'y', l*sym.sin(alpha))

beta, t = sym.symbols('beta t')

t = l*sym.cos(alpha)/v0*sym.cos(beta)
fy = sym.Eq(v0*t*sym.sin(beta) - (g*t**2)/2, l*sym.sin(alpha))

rez = sym.nsolve(fy, beta, 0)
print(rez)

a = rez#[2]
print(a)

delta = a-alpha
print(delta)

real = v0**2 * sym.sin(delta) * sym.cos(delta) * 2 /g
print(real)

# plot
t = np.linspace(0, 1.2, 50)
fx = v0*t*sym.cos(a)
fy = v0*t*sym.sin(a) - (g*t**2)/2
plt.plot(fx, fy, '.', label=str(a) + ' rad')
plt.ylabel('višina/m')
plt.xlabel('dolžina/m')
#plt.xlim([0, 60])
#plt.ylim([-2, 2])
plt.legend(loc="best")
plt.grid()
plt.show()