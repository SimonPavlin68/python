import matplotlib.pyplot as plt
import numpy as np
from IPython.display import Audio, display

t = np.linspace(1, 130 ,44000)
zvizg = np.sin(t**2)
plt.plot(t, zvizg)
plt.xlim(1, 10)
plt.ylim(-2, 2)
plt.title('Žvižg')
plt.show()

#display(Audio(data=zvizg, rate=44000))