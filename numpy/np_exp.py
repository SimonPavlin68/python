import numpy as np
import sympy as sym

e = np.exp(3) #e**3
print(sym.N(e, 25))

e = 2.71828182846**3
print(sym.N(e, 25))