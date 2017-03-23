import pygame, math, sys
import random as rnd
from pygame.locals import *

BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

WIDTH = 400
HEIGHT = 400
STEP = 20
RADIUS = 10
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill(WHITE)

counter = 0
Matrix = [[0 for x in range(int(WIDTH/STEP))] for y in range(int(HEIGHT/STEP))]

def init():
    for i in range(0, WIDTH, STEP):
        pygame.draw.line(screen, BLACK, [i, 0], [i, HEIGHT], 1)
    for j in range(0, HEIGHT, STEP):
        pygame.draw.line(screen, BLACK, [0, j], [WIDTH, j], 1)
    pygame.display.update()


def printMatrix():
    for j in range(int(WIDTH/STEP)):
        print(Matrix[j])


def checkBoat(len, x, y , hor):
    for i in range(len):
        if(hor):
            if (Matrix[x+i][y] > 0):
                print('colision')
                return False
        else:
            if (Matrix[x][y+i] > 0):
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
        print(xr, yr, horizontal)
        if(checkBoat(length, xr, yr, horizontal)):
            for i in range(length):
                if(horizontal):
                    Matrix[xr+i][yr] = length
                else:
                    Matrix[xr][yr+i] = length
            break;


def hit(mx, my):
    print(mx,my)
    x = math.floor(mx / STEP)
    y = math.floor(my / STEP)

    if(Matrix[x][y] > 0):
        pygame.draw.rect(screen, RED, [x * STEP, y * STEP, STEP, STEP])
    else :
        pygame.draw.rect(screen, BLUE, [x * STEP, y * STEP, STEP, STEP])
    pygame.display.update()

init()
initboat(6)
initboat(5)
initboat(4)
initboat(4)
initboat(3)
initboat(3)
initboat(2)
printMatrix()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            posx, posy = pygame.mouse.get_pos()
            counter += 1
            print(counter)
            hit(posx, posy)
