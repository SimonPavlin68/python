import numpy as np
import sympy as sym
import matplotlib.pyplot as plt

g = 9.81    # gravitacijski pospešek
v0 = 10     # začetna hitrost
alpha = 35  # kot
h = 3       # začetna višina
time = np.linspace(0, 2, 20)

def fx(t):
    return v0*t*sym.cos(np.deg2rad(alpha))

def fy(t):
    return h + v0*t*sym.sin(np.deg2rad(alpha)) - (g*t**2)/2

x = []
y = []
yr = []
for i in time:
    x.append(fx(i))
    y.append(fy(i))
    yr.append(fy(i) + np.random.randint(11)/5 -1)
x = np.asarray(x)
y = np.asarray(y)
yr = np.asarray(yr)

# aproksimacija
a, b, c = np.polyfit(time, yr, deg=2)

# ničla
from scipy import optimize
root = optimize.newton(fy, 1.5)
print('optimize.newton', fx(root))

# odvod
t = sym.symbols('t')
fd = sym.diff(fy(t), t)
print(fd)
#nicla = optimize.newton(fd, 1.5)

# plot
plt.plot(x, y, 'g', label='funkcija', linewidth=2)
plt.plot(x, yr, 'bo', label='deviacija')
plt.plot(x, a*time**2 + b*time + c, 'r', label='aproksimacija', linewidth=2)

plt.xlabel('$dolžina$')
plt.ylabel('$višina$')
plt.axhline(y=0, linewidth=1, color='k')
plt.axvline(x=fx(root), linewidth=1, color='k')
plt.legend(loc="best")
plt.grid()
plt.show()

