import pygame, math, sys
import random as rnd
from pygame.locals import *

BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

WIDTH = 200
HEIGHT = 200
STEP = 20
RADIUS = 10
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill(WHITE)

counter = 0
Matrix = [[0 for x in range(int(WIDTH/STEP))] for y in range(int(HEIGHT/STEP))]
boats = []

def boat(submerged, coordinates):
    submerged = False
    coordinates = []

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
        if(checkBoat(length, xr, yr, horizontal)):
            coordinates = []
            for i in range(length):
                if(horizontal):
                    Matrix[yr][xr+i] = length
                    coordinates.append([yr, xr+i, 0])
                else:
                    Matrix[yr+i][xr] = length
                    coordinates.append([yr+i, xr, 0])
            boats.append(boat(False, coordinates))
            break;


def hit(mx, my):
    print(mx,my)
    x = math.floor(mx / STEP)
    y = math.floor(my / STEP)

    color = BLUE
    if(Matrix[y][x] > 0):
        color = RED
    pygame.draw.rect(screen, color, [x * STEP, y * STEP, STEP, STEP])
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
print(boats)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            posx, posy = pygame.mouse.get_pos()
            counter += 1
            print(counter)
            hit(posx, posy)
