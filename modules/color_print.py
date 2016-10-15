def printColor(text, color):
    if color == 'red':
        print(RED + text + END, end='')
    elif color == 'green':
        print(GREEN + text + END, end='')
    elif color == 'blue':
        print(BLUE + text + END, end='')
    else:
        print(text, end='')

RED = '\033[31m'
GREEN = '\033[32m'
BLUE = '\033[34m'
END = '\033[0m'

#import colorama as cr
from colorama import Fore, Back, Style

print(Fore.GREEN + 'Green text')
print(Fore.RED + 'Red text')
print(Fore.RESET + 'xx')
print(Back.MAGENTA + 'Red text'+ Back.RESET)
print('a')