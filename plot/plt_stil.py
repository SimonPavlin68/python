import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2, 100)

plt.plot(x, x, label = 'linear', linewidth = 2)
plt.plot(x, x**2, '--', label = 'quadratic', linewidth = 2)
plt.plot(x, x**3, '.', label = 'cubic', linewidth = 2)

plt.xlabel('X label')
plt.ylabel('Y label')

plt.title("Simple Plot")

#plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.05), ncol=3, fancybox=True, shadow=True)
#plt.legend(loc='upper left', fancybox=True, shadow=True)
#plt.legend(loc = 'upper left', fancybox=True)
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))

# Shrink current axis by 20%
ax = plt.subplot()
box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])

plt.show()