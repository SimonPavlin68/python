from python.classes.pravokotnik import Pravokotnik
#from python.classes.CetrtinaKroga import CetrtinaKroga

p = Pravokotnik(3,4)

print(p.izpis())
print('površina: ', p.povrsina())
print('diagonala:', p.diagonala())
print('obseg:    ', p.obseg())
print('višina:   ', p.visina)
print(':__dict__ ', p.__dict__)
print('kvadrat?  ', p.jeKvadret())

#R = 10
#h = 11

#ck = CetrtinaKroga(R, h)
#print(sorted(ck.__dict__.keys()))
#print(ck.izracunaj_volumen())
#print(sorted(ck.__dict__.keys()))