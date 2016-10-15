import random
import modules.pravokotnik as pravokotnik

a = random.randint(2, 4)
b = random.randint(3, 5)
print('a={0} b={1}'.format(a,b))

print('ploščina: ', pravokotnik.ploscina(a, b))
print('obseg: ', pravokotnik.obseg(a, b))
print('diagonala:', pravokotnik.diagonala(a, b))
print('kvadrat? ', pravokotnik.jeKvadrat(a, b))