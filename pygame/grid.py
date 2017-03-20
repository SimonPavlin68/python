import pygame, math, sys
import random as rnd
import numpy as np
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
ladja = np.

def init():
    for i in range(0, WIDTH, STEP):
        pygame.draw.line(screen, BLACK, [i, 0], [i, HEIGHT], 1)
    for j in range(0, HEIGHT, STEP):
        pygame.draw.line(screen, BLACK, [0, j], [WIDTH, j], 1)
    pygame.display.update()

def initboat():
    xr = rnd.randint(0, 15)
    yr = rnd.randint(0, 15)
    smer = rnd.getrandbits(1)
    print(xr, yr, smer)


def hit(x, y):
    pygame.draw.rect(screen, BLUE, [math.floor(x/STEP)*STEP, math.floor(y/STEP)*STEP, STEP, STEP])
    pygame.display.update()

init()
initboat()

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
