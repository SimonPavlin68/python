import pygame, math
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

WIDTH = 800
HEIGHT = 600

BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

vertices = (
    (0, 0, 0),
    (0, 1, 0),
    (-1, -1, 1),
    (1, -1, 1),
    (0, -1, -1)
    )

colors = (
    RED,
    BLACK,
    BLACK,
    BLACK,
    BLACK
    )


def points():
    glPointSize(5)
    #glColor(BLACK)
    #glColor3f(1.0, 0.0, 0.0);
    glBegin(GL_POINTS);
    x = 0
    for v in vertices:
        glColor3fv(colors[x])
        x += 1
        glVertex3fv(v);
    glEnd();


def main():
    pygame.init()
    pygame.display.set_mode((WIDTH, HEIGHT), DOUBLEBUF|OPENGL)
    pygame.display.set_caption("Points")

    gluPerspective(50, (WIDTH/HEIGHT), 0.1, 50.0)

    glTranslatef(0.0,0.0,-5)

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glRotatef(1, 1, 1, 1) # angle, x, y, z

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        glClearColor(1.0, 1.0, 1.0, 1.0);
        points()
        pygame.display.flip()
        clock.tick(60)

main()