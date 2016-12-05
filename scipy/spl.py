import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import InterpolatedUnivariateSpline

n = 5
x = np.arange(n, dtype=int)
y = [1,2,1,2,1]
plt.plot(x, y, 'ro', label='interpolacijske točke')

xint = np.linspace(np.min(x), np.max(x), 100)
spl = InterpolatedUnivariateSpline(x, y, k=3) # poglejte opcije!
#spl1 = spl.derivative(1)
plt.plot(xint, spl(xint), label='Kubični zlepek');
#plt.plot(xint, spl1(xint), label='Prvi odvod')
plt.legend(loc='best')
plt.show()
print(spl.get_knots())
