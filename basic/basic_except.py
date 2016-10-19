cifre = [1, 2, 3, 0, 4]

try:
    for i in cifre:
        print(1/i)
except ZeroDivisionError as e:
    print('nea gre:', str(e))
except:
    print('except')

try:
    for i in cifre:
        print(i)
        if(i == 3):
            raise Exception('Vržena izjema')
except Exception as e:
    print('Ujeta izjema: ', str(e))