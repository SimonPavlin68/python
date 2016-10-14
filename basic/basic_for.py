imena = ['Janko', 'Metka', 'Sneguljčica', 'Peter Pan']

print('--- seznam ---')
for ime in imena:
    print(ime)

enote = {'dolžina': 'm', 'masa': 'kg', 'čas': 's'}

print('--- več spremenljivk ---')
for key, value in enote.items():
    print('{0} - {1}'.format(key, value))

print('--- range ---')
for i in range(3):
    print(i)

print('--- enumerate ---')
for i, ime in enumerate(imena):
    print(i, ime)

print('--- zip ---')
liki = ['krog', 'trikotnik', 'pravokotnik']
barve = ['rdeč', 'moder', 'zelen']
for barva, lik in zip(barve, liki):
    print(barva, lik)