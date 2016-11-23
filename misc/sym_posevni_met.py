import sympy as sym
import numpy as np
import matplotlib.pyplot as plt

g = 9.81
v0 = 10
alpha = 15
h = 0

def plot(a):
    t = np.linspace(0, 2, 50)
    fx = v0*t*sym.cos(np.deg2rad(a))
    fy = h + v0*t*sym.sin(np.deg2rad(a)) - (g*t**2)/2
    plt.plot(fx, fy, '.', label=str(a) + ' deg')

for i in range(-1, 6, 1):
    plot(i*alpha)

plt.ylabel('višina/m')
plt.xlabel('dolžina/m')
plt.xlim([0, 12])
plt.ylim([-6, 6])
plt.legend(loc="best")
plt.grid()
plt.show()