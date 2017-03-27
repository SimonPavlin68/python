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
    (-1, -1, 1),
    (-1, 1, 1)
    )

edges = (
    (0,1),
    (0,3),
    (0,4),
    (2,1),
    (2,3),
    (2,7),
    (6,3),
    (6,4),
    (6,7),
    (5,1),
    (5,4),
    (5,7)
    )

surfaces = (
    (0,1,2,3),
    (3,2,7,6),
    (6,7,5,4),
    (4,5,1,0),
    (1,5,7,2),
    (4,0,3,6)
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
    display = (WIDTH, HEIGHT)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    pygame.display.set_caption("Cube translate")

    gluPerspective(50, (display[0]/display[1]), 0.1, 50.0)

    glTranslatef(0.0,0.0,-5)

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    glTranslatef(-0.5, 0, 0)
                if event.key == pygame.K_RIGHT:
                    glTranslatef(0.5, 0, 0)

                if event.key == pygame.K_UP:
                    glTranslatef(0, 1, 0)
                if event.key == pygame.K_DOWN:
                    glTranslatef(0, -1, 0)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4: #wheel in
                    glTranslatef(0, 0, 1.0)

                if event.button == 5: #wheel out
                    glTranslatef(0, 0, -1.0)

        #glRotatef(1, 1, 1, 1) # angle, x, y, z
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        glClearColor(1.0, 1.0, 1.0, 1.0);
        cube()
        pygame.display.flip()
        clock.tick(60)

main()