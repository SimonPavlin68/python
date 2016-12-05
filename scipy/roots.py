import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return x**3 - 10*x**2 +5

x_r = np.linspace(-2, 2 ,100)
plt.axhline(0, color='r')
plt.plot(x_r, f(x_r))
plt.plot(x_r, np.tan(x_r))

plt.grid()
plt.show()


def inkrementalna(fun, x1, x2, dx):
    x_d = np.arange(x1, x2, dx)  # pripravimo x vrednosti
    f_d = np.sign(fun(x_d))  # pripravimo predznake funkcije
    f_d = f_d[1:] * f_d[:-1]  # vektorsko odštejemo
    i = np.argmin(f_d)  # prvi prehod skozi ničlo
    return np.asarray([x_d[i], x_d[i + 1]])

rez = inkrementalna(f, 0., 1., 0.001)
print(rez)


def inkrementalna_super(fun, x1, x2, iteracij=3):
    for i in range(iteracij):
        dx = (x2 - x1) / 10
        x1, x2 = inkrementalna(fun, x1, x2, dx)
    return np.asarray([x1, x2])

rez8 = inkrementalna_super(f, 0., 1., iteracij=8)
print(rez8)