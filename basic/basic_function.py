def površina(dolžina, širina):
    return dolžina * širina

print('Ploščina je: {0}'.format(površina(3, 4)))

print() #prazna vrstica

def povrsina(dolzina = 5, sirina = 5):
    """
    :param dolzina:
    :param sirina:
    :return povrsina
    """
    return dolzina * sirina

print('Ploščina je: {0}'.format(povrsina(3, 4)))
print('Ploščina je: {0}'.format(povrsina(3)))
print('Ploščina je: {0}'.format(povrsina()))
print('Ploščina je: {0}'.format(povrsina(sirina = 6)))
print('Ploščina je: {0}'.format(povrsina(sirina = 6, dolzina = 6)))