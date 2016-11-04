import numpy as np
class CetrtinaKroga:

    def __init__(self, Polmer, Debelina):
        self.polmer = Polmer
        self.debelina = Debelina

    def izracunaj_volumen(self):
        self.volumen = self.debelina*np.pi*self.polmer**2/4
        return self.volumen