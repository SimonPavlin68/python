import numpy as np
import sympy as sym
import matplotlib.pyplot as plt

g = 9.81    # gravitacijski pospešek
v0 = 10     # začetna hitrost
alpha = 40  # kot
h = 3       # začetna višina
time = np.linspace(0, 2, 20)

t = sym.symbols('t')
def fx(t):
    return v0*t*sym.cos(np.deg2rad(alpha))
def fy(t):
    return h + v0*t*sym.sin(np.deg2rad(alpha)) - g*(t**2)/2
def dfy(tim):
    return sym.diff(fy(tim), t)

fxl = sym.lambdify(t, fx(t), modules=['numpy'])
fyl = sym.lambdify(t, fy(t), modules=['numpy'])
fydl = sym.lambdify(t, dfy(t), modules=['numpy'])

y_random = []
for i in time:
    y_random.append(fy(t).subs({t: i}) + np.random.randint(11)/5 -1)
y_random = np.asarray(y_random)

# aproksimacija
a, b, c = np.polyfit(time, y_random, deg=2)

# ničla
from scipy import optimize
root1 = optimize.newton(fy, 1.5)
#print('optimize.newton', root1)

# ničla odvoda
test = False
if(test):
    root2 = optimize.newton(dfy, 0.58)
else:
    def fyd(t):
        return v0*sym.sin(np.deg2rad(alpha)) - g*t
    root2 = optimize.newton(fyd, 0.5)
#print('optimize.newton', root2)

# plot
plt.plot(fxl(time), fyl(time), 'b', label='$funkcija\\ (poševni\\ met)$', linewidth=2)
#plt.plot(fxl(time), fyl(time), 'b', label='$y(t) = h+v0*t*sin(\\alpha) - g*t^2/2$', linewidth=2)
plt.plot(fxl(time), y_random, 'ro', label='$deviacija$')
plt.plot(fxl(time), a*time**2 + b*time + c, 'g', label='$aproksimacija$', linewidth=3)
plt.plot(fxl(time), fydl(time), 'r', label='$odvod\\ funkcije$')

plt.xlabel('$dolžina/m$')
plt.ylabel('$višina/m$')
plt.axhline(y=0)
plt.axvline(x=fx(root1)) #največja dolžina (y=0)
plt.axvline(x=fx(root2))
plt.axhline(y=fy(root2)) #največja višina
plt.legend(loc="best")
plt.grid()
plt.show()

