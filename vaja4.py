from python.classes.CetrtinaKroga import CetrtinaKroga
import numpy as np
import sympy as sym


R = 10
H = 11
N = 7

ck = CetrtinaKroga(R, H)
print(sorted(ck.__dict__.keys()))
print(ck.izracunaj_volumen())
print(sorted(ck.__dict__.keys()))

print(sym.E.evalf(n=N))

h, r = sym.symbols('h, r')
V = H*np.pi*R**2/4

print(sym.N(V, N))