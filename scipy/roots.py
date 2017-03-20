import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return x**3 - 10*x**2 + 5

x_r = np.linspace(-2, 2 ,100)
plt.axhline(0, color='r')
plt.plot(x_r, f(x_r))
plt.plot(x_r, np.tan(x_r))

plt.grid()
#plt.show()


def inkrementalna(fun: object, x1: object, x2: object, dx: object) -> object:
    x_d = np.arange(x1, x2, dx)  # pripravimo x vrednosti
    f_d = np.sign(fun(x_d))  # pripravimo predznake funkcije
    f_d = f_d[1:] * f_d[:-1]  # vektorsko odštejemo
    i = np.argmin(f_d)  # prvi prehod skozi ničlo
    return np.asarray([x_d[i], x_d[i + 1]])

rez1 = inkrementalna(f, 0., 1., 0.001)
print('inkrementalna 1', rez1)


def inkrementalna_super(fun, x1, x2, iteracij=3):
    for i in range(iteracij):
        dx = (x2 - x1) / 10
        x1, x2 = inkrementalna(fun, x1, x2, dx)
    return np.asarray([x1, x2])

rez2 = inkrementalna_super(f, 0., 1., iteracij=8)
print('inkrementalna 2', rez2)


def bisekcija(fun, x1, x2, tol=1e-3):
    n = np.ceil(np.log(np.abs(x2 - x1) / tol) / np.log(2)).astype(int)  # števil iteracij
    for i in range(n):
        x3 = (x1 + x2) / 2
        if np.sign(fun(x3)) != np.sign(fun(x1)):
            x2 = x3
        else:
            x1 = x3
    return (x1 + x2) / 2

rez2 = bisekcija(f, 0, 1, tol=1e-7)
print('bisekcija      ', rez2)

from scipy import optimize

rez3 = optimize.bisect(f, 0, 1, xtol=1e-7)
print('optimize.bisect', rez3)

def sekantna(fun, x1, x2, tol=1e-3, max_iter=50):
    for i in range(max_iter):
        f1 = fun(x1)
        f2 = fun(x2)
        x3 = x2 + f2 * (x2 - x1) / (f1 - f2)
        x1 = x2
        x2 = x3
        if np.abs(x2 - x1) < tol:
            return (x1 + x2) / 2
    raise Exception('Metoda po {:g} iteracijah ne konvergira'.format(max_iter))

rez4 = sekantna(f, 0, 1., tol=1.e-7)
print('sekantna       ', rez4)

rez5 = optimize.newton(f, 0.1)
print('optimize.newton', rez5)

rez6 = optimize.ridder(f, 0, 1)
print('optimize.ridder', rez6)

def newton_raphson(fun, dfun, x0, tol=1e-3, max_iter=50):

    for i in range(max_iter):
        x1 = x0 - fun(x0) / dfun(x0)
        if np.abs(x1 - x0) < tol:
            return x1
        x0 = x1
    raise Exception('Metoda po {:g} iteracijah ne konvergira'.format(max_iter))

#rez7 = optimize.ridder(f, 0, 1)
#print('newton_raphson ', rez7)

def df(x):
    return 3*x**2 - 20*x
def ddf(x):
    return 6*x - 20

rez8 = newton_raphson(f, df, 1, tol=1e-7)
print('newton_raphson ', rez8)

rez9 = optimize.newton(f, 1, df)
print('ffff: ',type(f))
print('optimize.newton', rez9)

rez10 = optimize.newton(f, 1, df, fprime2=ddf)
print('optimize.newton', rez10)

#import sympy as sym
#x, y = sym.symbols('x, y')
#sol = sym.solve([x**3 + y -2, y**2 - 4], x, y)
#print(sol)

rez11 = optimize.root(f, [0, 1])
print(rez11)