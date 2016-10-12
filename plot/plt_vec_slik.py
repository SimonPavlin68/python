import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10 , 100)

y1 = np.sin(x)
y2 = np.sin(x+1)
y3 = np.sin(x**1.2)

#colors = ('b', 'g', 'r', 'c', 'm', 'y', 'k')
#linestyles = ['_', '-', '--', ':']

plt.subplot(2,3,1)
plt.plot(x, y1, 'r--', linewidth = 2)
plt.subplot(2,3,2)
plt.plot(x, y2, 'g^', linewidth = 3)
plt.subplot(2,3,3)
plt.plot(x, y2*y3, 'bs', linewidth = 2)
plt.subplot(2,3,4)
plt.plot(x, y2 + y3, 'c:', linewidth = 3)
plt.subplot(2,3,5)
plt.plot(x, y3, 'mo', linewidth = 2)
plt.subplot(2,3,6)
plt.plot(x, y1 - y3, 'y', linewidth = 3)
plt.plot(x, y1 - y2 + y3, 'k_', linewidth = 3)
plt.grid()

plt.show()