import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import sympy as sym

n = 10 #
Q_1 = -29.4 # °C
Q_2 = -18.4 # °C
Q_3 = -9 # °C
Q_4 = 8.4 # °C
Q_5 = 19.3 # °C
Q_6 = 28.9 # °C
#s = 2 #
t_1 = 51.9 # s
t_2 = 62 # s
t_3 = 71.3 # s
t_4 = 80.6 # s
t_5 = 90.6 # s
t_6 = 99.6 # s
t_s = 75.2 # s
t_u = 83 # s

Q = np.asarray([Q_1, Q_2, Q_3, Q_4, Q_5, Q_6])
t = np.asarray([t_1, t_2, t_3, t_4, t_5, t_6])

plt.plot(t, Q, 'ro');
plt.axhline(0, color='k', linewidth=1);
plt.axvline(t_s, color='r', linewidth=1);

# naloga 4:

m = 2 #stopnja
A = np.zeros((m+1,m+1))
for v in range(m+1):
    for s in range(m+1):
        A[v,s] = np.sum(t**(2*m-v-s))
b = np.zeros(m+1)
for v in range(m+1):
    b[v] = np.dot(Q,t**(m-v))

#print(A)
#print(b)

a = np.linalg.solve(A, b)

# odgovor 4
odg4 = a
print(odg4, type(odg4))

y_app = np.sum(np.asarray([_*t**(m-i) for i,_ in enumerate(a)]), axis=0)

y_m = np.zeros(6)
def my_func(t, A, B, C):
    return A*t**2 + B*t + C

for i in range(6):
    y_m[i] = my_func(t[i], a[0], a[1], a[2])

#print(y_m)

plt.plot(t, Q, 'ro')
plt.plot(t, y_app, 'b', lw=3);
plt.plot(t, y_m, 'w', lw=1);
plt.show()

# naloga 6:
T = sym.symbols('T')
en = sym.Eq(a[0]*T**2 + a[1]*T + a[2], 0)
odg6 = sym.solve(en, [T])[1]

print(odg6, type(odg6))