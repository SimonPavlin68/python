import pygame
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

vertices = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, 1, 1),
    (-1, -1, 1)
    )

edges = (
    (0,1),
    (0,3),
    (0,4),
    (2,1),
    (2,3),
    (2,6),
    (7,3),
    (7,4),
    (7,6),
    (5,1),
    (5,4),
    (5,6)
    )

surfaces = (
    (0,1,2,3),
    (3,2,6,7),
    (7,6,5,4),
    (4,5,1,0),
    (1,5,6,2),
    (4,0,3,7)
    )
colors = (
    RED,
    BLUE,
    GREEN,
    RED,
    BLUE,
    GREEN,
    RED,
    BLUE,
    GREEN,
    RED,
    BLUE,
    GREEN
    )


def cube():
    glBegin(GL_QUADS)
    for surface in surfaces:
        x = 0
        for vertex in surface:
            x += 1
            glColor3fv(colors[x])
            glVertex3fv(vertices[vertex])
    glEnd()

    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glColor(BLACK)
            glVertex3fv(vertices[vertex])
    glEnd()


def main():
    pygame.init()
    pygame.display.set_mode((WIDTH, HEIGHT), DOUBLEBUF|OPENGL)
    pygame.display.set_caption("Cube rotate")

    gluPerspective(50, (WIDTH/HEIGHT), 0.1, 50.0)

    glTranslatef(0.0,0.0,-5)

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        #glRotatef(1, 1, 1, 1) # angle, x, y, z

        x = glGetDoublev(GL_MODELVIEW_MATRIX)
        print(x)


        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        glClearColor(1.0, 1.0, 1.0, 1.0);

        glTranslatef(0, 0, 0.1)
        cube()
        pygame.display.flip()
        clock.tick(6)

main()