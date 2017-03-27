import pygame
import math

pygame.init()
screen = pygame.display.set_mode((400, 400))
done = False

BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

x = 200
y = 200
LENGTH = 100
alpha = 0

clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pressed = pygame.key.get_pressed()
    #if pressed[pygame.K_UP]: y -= 3
    #if pressed[pygame.K_DOWN]: y += 3
    if pressed[pygame.K_LEFT]: alpha -= 3
    if pressed[pygame.K_RIGHT]: alpha += 3

    screen.fill(WHITE)

    pygame.draw.line(screen, BLACK, [x, y], [x + LENGTH * math.cos(math.radians(alpha)), y + LENGTH * math.sin(math.radians(alpha))], 1)
    pygame.draw.line(screen, RED, [x, y], [x + LENGTH * math.sin(math.radians(alpha)), y - LENGTH * math.cos(math.radians(alpha))], 1)
    pygame.draw.line(screen, GREEN, [x + LENGTH * math.cos(math.radians(alpha)), y + LENGTH * math.sin(math.radians(alpha))],
                     [x + math.sqrt(2)*LENGTH * math.sin(math.radians(alpha+45)), y - math.sqrt(2)*LENGTH * math.cos(math.radians(alpha+45))], 1)
    pygame.draw.line(screen, BLUE, [x + math.sqrt(2) * LENGTH * math.sin(math.radians(alpha + 45)),
                      y - math.sqrt(2) * LENGTH * math.cos(math.radians(alpha + 45))], [x + LENGTH * math.sin(math.radians(alpha)), y - LENGTH * math.cos(math.radians(alpha))], 1)

    pygame.display.flip()
    clock.tick(60)