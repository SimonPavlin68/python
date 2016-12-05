import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


def func(t, A, w, faza):
    return A*np.sin(w*t+faza)

t = np.linspace(0, 10, 10)
y = func(t, 1, 2, 3) + np.random.normal(scale=0.6, size=len(t))
plt.plot(t, y, 'or');
plt.show()

popt, pcov = curve_fit(func, t, y, p0=[1, 2.3, 1])
print(popt)
