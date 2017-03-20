import numpy as np
import sympy as sym
import matplotlib.pyplot as plt

A = 1.1 # m
l = 1.4 # m
n = 1000 # /
r = 1.1 # m

# odg 2

def func(alpha):
    return alpha**2 - A

def df(alpha):
    return 2*alpha

alpha = np.linspace(-3, 3, n)

from scipy import optimize
rez4 = optimize.newton(func, -0.1)
print('optimize.newton', rez4)
rez4a = optimize.newton(func, -0.1, df)
print('optimize.newton', rez4a)

#x_alpha = r * np.cos(alpha) + np.sqrt(l**2 - (r * np.sin(alpha))**2)
plt.plot(alpha, func(alpha))
plt.axhline(A, color='r')
plt.axhline(0, color='k')
plt.axvline(rez4a, color='k')
plt.show()

