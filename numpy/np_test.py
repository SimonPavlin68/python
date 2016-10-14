import numpy as np

a = np.zeros(3)
print(a)

b = np.arange(0,10)
print(b)
print(b[5])
print(b[-1])
print(b[2:7])

c = np.ones(5)
print(c)

print(b[::-1])

# matrike

m = np.zeros((5,3)) #5 vrstic, 3 stolpci
print(m)
print(np.ndim(m))
print(m[1])

a = [0, 1, 2, 3, 4, 5, 6, 7]
b = np.asarray(a)

print(a)
print(b)


