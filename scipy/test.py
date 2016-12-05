from scipy.interpolate import interp1d
import numpy as np
import matplotlib.pyplot as plt

#n = 3
#x = np.random.rand(n)
#x = np.sort(x)
#y = np.random.rand(n)
#plt.plot(x, y, 'ro')
#plt.show()

m = 23
n = 50

I = np.array([0.9,122.6,246.8,188.8,123.2,0.8,0.7000000000000001,39.3,105.3,246.7,138.1,0.8])
x = np.array([0,1,2,3,4,5,6,7,8,9,10,11])

xint = np.linspace(np.min(x), np.max(x), n)
print(xint)
#print(xint[-2])

f = interp1d(x, I, kind='cubic')
xnew = np.linspace(x[0], x[-1], 50)
#xnew = np.linspace(np.min(x), np.max(x), 50)
Inew = f(xnew)   # uporabimo interpolacijsko funkcijo dobljeno z `interp1d`

rez = 0
for i in range(m):
    rez = rez + Inew[i]
    print(i, rez)
print(rez)
plt.plot(x, I, 'o', xnew, Inew, '-')
plt.show()


#plt.plot(x, I, 'ro')
#plt.show()

#a = np.ndarray(1)
#a[0] = 0.9
#print(type(a))
#print(a)
