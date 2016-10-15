import matplotlib.pyplot as plt
import numpy as np

x = np.random.normal(size=10000)
plt.hist(x)

#ax = plt.gca()

plt.show()