from classes.pravokotnik import Pravokotnik

class Kvadrat(Pravokotnik):

    def __init__(self, a):
        super().__init__(a=a, b=a)