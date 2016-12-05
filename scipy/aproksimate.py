import numpy as np
import matplotlib.pyplot as plt

n = 50
k = 2.
c = 2.
x = np.linspace(0, 1, n)
y = k*x + c + np.random.normal(scale=0.25, size=len(x))


#plt.plot(x, y, 'o')
#plt.show()

#A = [[np.sum(x**2), np.sum(x)], [np.sum(x), len(x)]]
#b = [np.dot(y,x), np.sum(y)]
#A = np.asarray(A)
#b = np.asarray(b)
#print('A:', A)
#print('b:', b)

#a0, a1 = np.linalg.solve(A, b)

a0, a1 = np.polyfit(x, y, deg=1)

plt.plot(x,y, 'ro')
plt.plot(x, a0*x + a1)
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.show()