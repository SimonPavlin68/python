import pygame, math, sys, time
import random as rnd
from classes.boat import Boat


BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

WIDTH = 300
HEIGHT = 300
STEP = 20
RADIUS = 10
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill(WHITE)

counter = 0
Matrix = [[0 for x in range(int(WIDTH/STEP))] for y in range(int(HEIGHT/STEP))]
boats = []
konc = False

def init():
    for i in range(0, WIDTH, STEP):
        pygame.draw.line(screen, BLACK, [i, 0], [i, HEIGHT], 1)
    for j in range(0, HEIGHT, STEP):
        pygame.draw.line(screen, BLACK, [0, j], [WIDTH, j], 1)
    pygame.display.update()


#def printMatrix():
#    for j in range(int(WIDTH/STEP)):
#        print(Matrix[j])


def checkboat(len, x, y , hor):
    for i in range(len):
        if(hor):
            if (Matrix[y][x+i] > 0):
                print('colision')
                return False
        else:
            if (Matrix[y+i][x] > 0):
                print('colision')
                return False
    return True

def initboat(length):
    while True:
        horizontal = rnd.choice([True, False])
        if(horizontal):
            xr = rnd.randint(0, int(WIDTH/STEP)-length-1)
            yr = rnd.randint(0, int(HEIGHT/STEP)-1)
        else:
            xr = rnd.randint(0, int(WIDTH/STEP)-1)
            yr = rnd.randint(0, int(HEIGHT/STEP)-length-1)
        print(length, xr, yr, horizontal)
        if(checkboat(length, xr, yr, horizontal)):
            coordinates = []
            for i in range(length):
                if(horizontal):
                    Matrix[yr][xr+i] = length
                    coordinates.append([xr+i, yr, 0])
                else:
                    Matrix[yr+i][xr] = length
                    coordinates.append([xr, yr+i, 0])
            b = Boat(coordinates, horizontal)
            boats.append(b)
            break;


def hit(mx, my):
    x = math.floor(mx / STEP)
    y = math.floor(my / STEP)
    for b in boats:
        if(b.hit(screen, STEP, [x, y])):
            if(gameover()):
                return True
    if(Matrix[y][x] == 0):
        pygame.draw.rect(screen, BLUE, [x * STEP, y * STEP, STEP, STEP])
        pygame.display.update()
        playsound("Splash.wav")
    return False

def gameover():
    for b in boats:
        if(not b.submerged):
            return False
    print('gameover', counter)
    pygame.font.init()
    myfont = pygame.font.SysFont('Comic Sans MS', 30)
    textsurface = myfont.render('GAME OVER', False, BLACK)
    print(textsurface.get_rect().width, textsurface.get_rect().height)
    screen.blit(textsurface,((WIDTH - textsurface.get_rect().width) / 2, HEIGHT / 2 - textsurface.get_rect().height / 2))
    pygame.display.update()
    return True


def playsound(sound):
    pygame.mixer.init()
    sound = pygame.mixer.Sound(sound)
    sound.play()

init()
initboat(6)
initboat(5)
initboat(4)
initboat(4)
initboat(3)
initboat(3)
initboat(2)
#printMatrix()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if(not konc):
                posx, posy = pygame.mouse.get_pos()
                counter += 1
                if(hit(posx, posy)):
                    konc = True
