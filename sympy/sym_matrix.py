import sympy as sym
import math

A11, A12, A21, A22 = sym.symbols('A11, A12, A21, A22')
x1, x2 = sym.symbols('x1, x2')
b1, b2 = sym.symbols('b1, b2')

A = sym.Matrix([[A11, A12], [A21, A22]])
x = sym.Matrix([[x1], [x2]])
b = sym.Matrix([[b1], [b2]])

eq = sym.Eq(A*x, b)

print(sym.solve(eq, [x1, x2]))

print(A.det())

parametri = {A11: 1, A12: 2, A21: 2, A22: 4, b1: 1, b2: 2}

lin_odv = eq.subs(parametri)
print(lin_odv)
print(sym.solve(lin_odv), [x1, x2])
print(A.subs(parametri).det())

#------------------------------

B = A.subs(parametri)
print(B)
k = 0
for i in range(2):
    for j in range(2):
        k = k + B[i,j]**2
print(k)