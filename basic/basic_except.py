cifre = [1, 2, 3, 0, 4]

try:
    for i in cifre:
        print(1/i)
except ZeroDivisionError:
    print('nea gre')
except:
    print('except')

try:
    for i in cifre:
        print(i)
        if(i == 3):
            raise Exception('Dvignjena izjema')
except Exception as e:
    print('Ujeta izjema: ', str(e))