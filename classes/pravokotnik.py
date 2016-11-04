import math


class Pravokotnik:

    def __init__(self, a, b):
        # konstruktor
        self.sirina = a
        self.visina = b

    def set_sirina(self, sirina):
        self.sirina = sirina

    def set_visina(self, visina):
        self.visina = visina

    def povrsina(self):
        return self.sirina * self.visina

    def obseg(self):
        return 2*self.sirina + 2*self.visina

    def diagonala(self):
        return math.sqrt(self.sirina * self.sirina + self.visina * self.visina)

    def jeKvadret(self):
        return self.sirina == self.visina

    def izpis(self):
        if self.sirina == self.visina:
            return 'Kvadrat: stranica = {0}'.format(self.sirina)
        else:
            return 'Pravokotnik: širina = {0}, višina = {1}'.format(self.sirina, self.visina)

