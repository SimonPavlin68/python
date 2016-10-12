import numpy as np
import matplotlib.pyplot as plt
import random

x = range(0, 150, 10)

y1 = []
for a in x:
    y1.append(a / 2 + random.randint(-20, 20)/5)

y2 = [random.randint(-20, 20)/5 + (a / 2) for a in x]

y3 = [np.random.randint(-20, 20)/5 + (a / 2) for a in x]

plt.plot(x, y1, 'o', label='y1')
plt.plot(x, y2, 'o', label='y2')
plt.plot(x, y3, 'o', label='y3')

plt.legend(loc='upper left', fancybox=True, shadow=True)
plt.show()