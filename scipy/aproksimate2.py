import numpy as np
import matplotlib.pyplot as plt

#x = np.linspace(1, 5, 100)
#y = 2.*x**2 + 1.*x + 0. + np.random.normal(size=len(x))

Q_3 = -9 # °C
Q_4 = 8.4 # °C
Q_5 = 19.3 # °C
Q_6 = 28.9 # °C
t_3 = 71.3 # s
t_4 = 80.6 # s
t_5 = 90.6 # s
t_6 = 99.6 # s

y = np.asarray([Q_3, Q_4, Q_5, Q_6])
x = np.asarray([t_3, t_4, t_5, t_6])

m = 2 #stopnja
A = np.zeros((m+1,m+1))
for v in range(m+1):
    for s in range(m+1):
        A[v,s] = np.sum(x**(2*m-v-s))
b = np.zeros(m+1)
for v in range(m+1):
    b[v] = np.dot(y,x**(m-v))

print(A)
print(b)

a = np.linalg.solve(A, b)
print(a)
y_app = np.sum(np.asarray([_*x**(m-i) for i,_ in enumerate(a)]), axis=0)

plt.plot(x, y, 'ro')
plt.plot(x, y_app, lw=5, alpha=0.5);
plt.show()

print(np.polyfit(x, y, deg=2))