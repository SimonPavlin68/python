import numpy as np

a = [0, 1, 2, 3, 4, 5]
b = np.asarray(a)

print('list  a = ', a)
print('numpy b = ', b)

print('2 * a =   ', 3*a)
print('2 * b =   ', 3*b)
print('a + a =   ', a + a)
print('b + b =   ', b + b)
print('sin(a) =  ', np.sin(a))
print('sin(b) =  ', np.sin(b))

print(30*'-')
c = np.arange(5, dtype=int)
print('arrange dtype=int: ', c)

c = np.arange(5, dtype=float)
print('arrange dtype=float: ', c)

c = np.arange(5, dtype=complex)
print('arrange dtype=complex: ', c)

A = np.identity(3)
print('identity: A', A)
print('diagonal(A):' , np.diagonal(A))

A[1, 1] = 5 #priredi vrednost [vrstica, stolpec]
print(A)

print(np.trace(A)) #vsota po diagonali

print(30*'-')
A = np.array([[1, 2], [3, 2]])
B = np.array([[1, 1], [2, 2]])
x = np.array([1, 2])
y = np.array([3, 4])
print(A)
print(x)
print(np.transpose([x]))

#skalarni produkt
print('skalarni produkt: ', np.dot(x, y))
print(np.dot(A, x))
print(np.dot(A, y))
print(np.dot(A, B))

#vektorski produkt
print('vektorski produkt: ', np.cross(x, y))