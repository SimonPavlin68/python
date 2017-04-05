import pygame

WIDTH = 800
HEIGHT = 600

BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

pygame.init()
gameDisplay = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("first")
clock = pygame.time.Clock()
crashed = False

x = WIDTH * 0.5
y = HEIGHT * 0.5


def pic(x,y):
    img = pygame.image.load("angry.png")
    gameDisplay.blit(img,(x-img.get_width()/2,y-img.get_height()/2))

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
    gameDisplay.fill(WHITE)
    pic(x,y)
    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()