import sympy as sym
import numpy as np
import matplotlib.pyplot as plt

x = sym.symbols('x')

f1 = sym.sin(x)/x
fx = sym.series(f1, n=6)
print(fx)
f2 = sym.series(f1, n=6).removeO() # remove big O
print(f2)
f3 = sym.diff(f1, x)
f4 = sym.diff(f2, x)

f1l = sym.lambdify(x, f1, modules=['numpy'])
f2l = sym.lambdify(x, f2, modules=['numpy'])
f3l = sym.lambdify(x, f3, modules=['numpy'])
f4l = sym.lambdify(x, f4, modules=['numpy'])


t = np.linspace(-5.5, 5.5, 100)
plt.plot(t, f1l(t), 'b', label='sin(x)/x')
plt.plot(t, f2l(t), 'r', label='Taylor')
plt.plot(t, f3l(t), 'g', label='d/dx(sin(x)/x)')
plt.plot(t, f4l(t), 'k', label='d/dx(Taylor)')
plt.legend(loc='best')
plt.grid()
plt.show()

