import random

pogoj = random.choice([True, False])
i = random.randint(1, 7)
print('število: {0}, pogoj: {1}'.format(i, pogoj))

a = 'a'
b = 'b'
c = 'c'
d = 'd'

# if stavek
if i == 1:
    print('ena')
elif i == 2:
    print('dva')
elif i == 3:
    print('tri')
else:
    print('več od tri: ', i)

# if izraz
r = 'je res' if pogoj else 'ni res'
print(r)