import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10 , 100)

y1 = np.sin(x)
y2 = np.sin(x+1)
y3 = np.sin(x**1.2)

plt.plot(x, y1, 'r', linewidth = 2)
plt.plot(x, y2, 'g', linewidth = 2)
plt.plot(x, y3, 'b', linewidth = 2)
plt.grid()

plt.show()