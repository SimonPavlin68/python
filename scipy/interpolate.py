import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

n = 5
x = np.arange(n, dtype=int)
y = [-1,1,-1,1,-1]

f = interp1d(x, y, kind='cubic') #quadratic
xnew = np.linspace(x[0], x[-1], 100)
ynew = f(xnew)   # uporabimo interpolacijsko funkcijo dobljeno z `interp1d`
plt.plot(x, y, 'o', xnew, ynew, '-')
plt.axhline(0, color='k', linewidth=0.8);
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.show()

#x = np.linspace(0, np.pi/2, 4)
#y = np.sin(x)
#plt.plot(x, y, 'o-')
#plt.show()
