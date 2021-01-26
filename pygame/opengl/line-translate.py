import pygame, math
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

WIDTH = 800
HEIGHT = 600

BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)


def transform(position, angle):
    glTranslate(position[0], position[1], position[2])
    glRotate(angle, False, False, True) # angle, x, y, z


def draw(trans, angle):
    glPushMatrix()
    transform(trans, angle)
    glBegin(GL_LINES)
    glVertex3fv((0,0,0))
    glVertex3fv((1,0,0))
    glEnd()
    glPopMatrix()


def main():
    pygame.init()
    pygame.display.set_mode((WIDTH, HEIGHT), DOUBLEBUF|OPENGL)
    pygame.display.set_caption("Lines")

    gluPerspective(50, (WIDTH/HEIGHT), 0.1, 50.0)

    glTranslatef(0,0,-5)
    glLineWidth(2)
    glColor3fv(BLACK)

    clock = pygame.time.Clock()

    alpha = 0;
    beta = 0;
    step = 3
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if not hasattr(event, 'key'):
                continue
            if event.key == K_RIGHT:
                alpha -= step
            elif event.key == K_LEFT:
                alpha += step
            elif event.key == K_UP:
                beta += step
            elif event.key == K_DOWN:
                beta -= step
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        glClearColor(1.0, 1.0, 1.0, 1.0)

        draw((0, 0, 0), alpha)
        draw((math.cos(math.radians(alpha)), math.sin(math.radians(alpha)), 0), alpha+beta)
        beta-=1
        alpha+=1
        pygame.display.flip()
        clock.tick(60)

main()