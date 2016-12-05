import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import sympy as sym

n = 10 #
Q_3 = -9 # °C
Q_4 = 8.4 # °C
Q_5 = 19.3 # °C
Q_6 = 28.9 # °C
#s = 2 #
t_3 = 71.3 # s
t_4 = 80.6 # s
t_5 = 90.6 # s
t_6 = 99.6 # s
t_s = 75.2 # s
t_u = 83 # s

y = np.asarray([Q_3, Q_4, Q_5, Q_6])
t = np.asarray([t_3, t_4, t_5, t_6])


#plt.plot(t, Q, 'ro');
#plt.axhline(0, color='k', linewidth=1);
plt.axvline(t_u, color='b', linewidth=1);
plt.axvline(t_s, color='r', linewidth=1);
#plt.show()


def func(t, A, B, C):
    return A*t + np.exp(B*t + C)

plt.plot(t, y, 'ro')
y_app = func(t, -0.96763795, 0.02365867, 2.49665444)
plt.plot(t, y_app);

popt, pcov = curve_fit(func, t, y)

odg2 = popt
print('odg2', odg2, type(odg2))

# na n točk
k = (t_6-t_s)/(n-1)
odg3 = np.zeros(n)
for i in range(n):
    tmp = t_s+i*k
    print(tmp)
    odg3[i] = func(tmp, -0.96763795, 0.02365867, 2.49665444)
    plt.axvline(tmp, color='y', linewidth=1);

print('odg3', odg3)
print(y)
plt.show()

# naloga 5

#odg5 = func(t_u, -0.96777035, 0.02365718, 2.49690541)
#print(odg5, type(odg5))

