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
    (1, 0, 0),
    (0, 1, 0),
    (0, 0, 1),
    )

lines = (
    (0,1),
    (0,2),
    (0,3)
    )

colors = (
    RED,
    BLUE,
    GREEN
    )


def draw():
    glLineWidth(5)
    #glColor3fv(BLUE)
    glBegin(GL_LINES)
    x = 0
    for line in lines:
        glColor(colors[x])
        x += 1
        for vertex in line:
            glVertex3fv(vertices[vertex])
    glEnd()


def main():
    pygame.init()
    pygame.display.set_mode((WIDTH, HEIGHT), DOUBLEBUF|OPENGL)
    pygame.display.set_caption("Lines")

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
        glClearColor(1.0, 1.0, 1.0, 1.0)
        draw()
        pygame.display.flip()
        clock.tick(60)

main()