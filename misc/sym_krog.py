import sympy as sym
import numpy as np
import matplotlib.pyplot as plt

r = 10
x = sym.symbols('x')

fx = sym.lambdify(x, r*sym.sin(x), modules=['numpy'])
fy = sym.lambdify(x, r*sym.cos(x), modules=['numpy'])


fi = np.linspace(0, 90, 100)
plt.plot(fx(np.deg2rad(fi)), fy(np.deg2rad(fi)), 'b', label='krog')
plt.legend(loc='best')
plt.grid()
plt.show()