import sympy as sy
import numpy as np
from sympy.functions import sin,cos
import matplotlib.pyplot as plt

x = sy.Symbol('x')
f = sin(x)

def factorial(n):
    if n <= 0:
        return 1
    else:
        return n*factorial(n-1)


def taylor(function, x0, n):
    i = 0
    p = 0
    while i <= n:
        p = p + (function.diff(x, i).subs(x, x0))/(factorial(i))*(x - x0)**i
        i += 1
    return p

def plot():
    x_lims = [-5, 5]
    x1 = np.linspace(x_lims[0], x_lims[1], 800)
    y1 = []
    # Approximate up until 10 starting from 1 and using steps of 2
    for j in range(1, 10, 2):
        func = taylor(f, 0, j)
        print('Taylor expansion at n=' + str(j), func)
        for k in x1:
            y1.append(func.subs(x,k))
        plt.plot(x1, y1, label='order ' + str(j))
        y1 = []
    # Plot the function to approximate (sine, in this case)
    plt.plot(x1,np.sin(x1), label='sin of x')
    plt.xlim(x_lims)
    plt.ylim(x_lims)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend(loc="best")
    plt.grid(True)
    plt.title('Taylor series approximation')
    plt.show()

plot()
