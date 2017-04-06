import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

BLACK = (0, 0, 0)
RED = (1, 0, 0)
ORANGE = (1, 0.5, 0)
YELLOW = (1, 1, 0)
GREEN = (0, 1, 0)
BLUE = (0, 0, 1)
MAGENTA = (1, 0, 1)
WHITE = (1, 1, 1)

WIDTH = 800
HEIGHT = 600

def initGL(caption):
    pygame.init()
    pygame.display.set_mode((WIDTH, HEIGHT), DOUBLEBUF | OPENGL)
    pygame.display.set_caption(caption)

    glEnable(GL_DEPTH_TEST)     #Enable depth testing for z-culling
    #glLoadIdentity()
    gluPerspective(45, WIDTH/HEIGHT, 0.1, 100)
    #    eye  x, y, z
    #gluLookAt(0, 0, 0, 0, 0, -100, 0, 1, 0)


def transformation(position, scale, ang):
    glTranslatef(position[0], position[1], position[2])
    glRotate(ang, True, True, True)
    glScale(scale, scale, scale)


def cube(position, scale, ang):
    glPushMatrix()
    transformation(position, scale, ang)
    glBegin(GL_QUADS)
    glColor3fv(GREEN)
    glVertex3f(1, 1, -1)
    glVertex3f(-1, 1, -1)
    glVertex3f(-1, 1, 1)
    glVertex3f(1, 1, 1)
    glColor3fv(ORANGE)
    glVertex3f(1, -1, 1)
    glVertex3f(-1, -1, 1)
    glVertex3f(-1, -1, -1)
    glVertex3f(1, -1, -1)
    glColor3fv(RED)
    glVertex3f(1, 1, 1)
    glVertex3f(-1, 1, 1)
    glVertex3f(-1, -1, 1)
    glVertex3f(1, -1, 1)
    glColor3fv(YELLOW)
    glVertex3f(1, -1, -1)
    glVertex3f(-1, -1, -1)
    glVertex3f(-1, 1, -1)
    glVertex3f(1, 1, -1)
    glColor3fv(BLUE)
    glVertex3f(-1, 1, 1)
    glVertex3f(-1, 1, -1)
    glVertex3f(-1, -1, -1)
    glVertex3f(-1, -1, 1)
    glColor3fv(MAGENTA)
    glVertex3f(1, 1, -1)
    glVertex3f(1, 1, 1)
    glVertex3f(1, -1, 1)
    glVertex3f(1, -1, -1)
    glEnd()
    glPopMatrix()


def main():
    initGL("3D cubes")
    clock = pygame.time.Clock()

    glTranslatef(0, 0, -10)

    angle = 0;

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glClearColor(1, 1, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # Clear color and depth buffers

        for i in range(5):
            for j in range(5):
                #for k in range(5):
                cube((i-2, j-2, 0), 0.3, angle)

        glRotate(1, True, True, True)
        pygame.display.flip()
        clock.tick(60)

main()