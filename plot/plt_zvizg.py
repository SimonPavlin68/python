import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(1, 130 ,44000)
zvizg = np.sin(t**2)
plt.plot(t, zvizg)
plt.xlim(1, 10)
plt.ylim(-2, 2)
plt.title('Žvižg')
plt.show()

