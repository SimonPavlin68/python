import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10 , 100)

y1 = np.sin(x)
y2 = np.sin(x+1)
y3 = np.sin(x**1.2)

#colors = ('b', 'g', 'r', 'c', 'm', 'y', 'k', 'w')
#linestyles = ['_', '-', '--', ':', '^']

plt.subplot(2,2,1)
plt.grid()
plt.plot(x, y1, 'g--', linewidth = 3)

plt.subplot(2,2,2)
plt.grid()
plt.plot(x, y2, 'ro')

plt.subplot(2,2,3)
plt.grid()
plt.plot(x, y2*y3, 'b-', linewidth = 3)

plt.subplot(2,2,4)
plt.grid()
plt.plot(x, y2 + y3, 'k:', linewidth = 3)

#plt.subplot(2,3,5)
#plt.plot(x, y3, 'mo', linewidth = 2)
#plt.subplot(2,3,6)
#plt.plot(x, y1 - y3, 'y', linewidth = 3)
#plt.plot(x, y1 - y2 + y3, 'k_', linewidth = 3)

plt.show()