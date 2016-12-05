import sympy as sym
import math

x1, x2, x3 = sym.symbols('x1, x2, x3')

A = sym.Matrix([[1, -4, 1], [1, 6, -1], [2, -1, 2]])
print(A)
x = sym.Matrix([[x1], [x2], [x3]])
b = sym.Matrix([[7], [13], [5]])

eq = sym.Eq(A*x, b)

print(sym.solve(eq, [x1, x2]))

# Evklidova norma
k = 0
for i in range(3):
    for j in range(3):
        k = k + A[i,j]**2
print(math.sqrt(k))