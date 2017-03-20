import pygame, math, sys
from pygame.locals import *

BLACK = (0,0,0)
RED = (255,0,0)
WHITE = (255,255,255)

WIDTH = 640
HEIGHT = 480
RADIUS = 10
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill(WHITE)

x = 320
y = 240
xd = 1;
yd = -1;
pygame.draw.circle(screen, RED, (x,y), RADIUS)
pygame.display.update()

clock = pygame.time.Clock()

while True:
    clock.tick(100)
    x += xd
    y += yd
    screen.fill(WHITE)
    pygame.draw.circle(screen, RED, (x, y), 10)
    pygame.display.update()
    if (y <= RADIUS/2) or (y >= HEIGHT-RADIUS/2): yd *= -1
    if (x <= RADIUS/2) or (x >= WIDTH-RADIUS/2): xd *= -1
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
