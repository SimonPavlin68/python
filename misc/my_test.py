from sympy import *
import numpy as np
import matplotlib.pyplot as plt

#a = list([1, 2, 3])
#a.append(1)
#plt.plot(a)

class Seznam(list):

    def narisi(self):
        plt.plot(self, 'r.', label='besedilo')
        plt.legend()
        plt.xlim(-1, 6)
        plt.ylim(-1, 4)
        plt.show()

moj_seznam = Seznam([1,2,3])
moj_seznam.append(0)
moj_seznam.append(1)
moj_seznam.narisi()