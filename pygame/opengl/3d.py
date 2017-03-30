import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

WIDTH = 800
HEIGHT = 600

def initGL(caption):
    pygame.init()
    pygame.display.set_mode((WIDTH, HEIGHT), DOUBLEBUF | OPENGL)
    pygame.display.set_caption(caption)

    glEnable(GL_DEPTH_TEST)     #Enable depth testing for z-culling
    #glDepthFunc(GL_LEQUAL)
    #glShadeModel(GL_SMOOTH)
    #glHint(GL_PERSPECTIVE_CORRECTION_HINT, GL_NICEST)

    #glViewport(0, 0, WIDTH, HEIGHT)
    #glMatrixMode(GL_PROJECTION)
    #glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluPerspective(45, WIDTH/HEIGHT, 0.1, 100)
    #    eye  x, y, z
    #gluLookAt(0, 0, 0, 0, 0, -100, 0, 1, 0)


def cube(angle):
    glRotate(angle, True, True, True)
    glBegin(GL_QUADS)  # Begin drawing the color cube with 6 quads
    # Top face (y = 1)
    # Define vertices in counter-clockwise (CCW) order with normal pointing out
    glColor3f(0, 1, 0)  # Green
    glVertex3f(1, 1, -1)
    glVertex3f(-1, 1, -1)
    glVertex3f(-1, 1, 1)
    glVertex3f(1, 1, 1)
    # Bottom face (y = -1)
    glColor3f(1, 0.5, 0)  # Orange
    glVertex3f(1, -1, 1)
    glVertex3f(-1, -1, 1)
    glVertex3f(-1, -1, -1)
    glVertex3f(1, -1, -1)
    # Front face  (z = 1)
    glColor3f(1, 0, 0)  # Red
    glVertex3f(1, 1, 1)
    glVertex3f(-1, 1, 1)
    glVertex3f(-1, -1, 1)
    glVertex3f(1, -1, 1)
    # Back face (z = -1)
    glColor3f(1, 1, 0)  # Yellow
    glVertex3f(1, -1, -1)
    glVertex3f(-1, -1, -1)
    glVertex3f(-1, 1, -1)
    glVertex3f(1, 1, -1)
    # Left face (x = -1)
    glColor3f(0, 0, 1)  # Blue
    glVertex3f(-1, 1, 1)
    glVertex3f(-1, 1, -1)
    glVertex3f(-1, -1, -1)
    glVertex3f(-1, -1, 1)
    # Right face (x = 1)
    glColor3f(1, 0, 1)  # Magenta
    glVertex3f(1, 1, -1)
    glVertex3f(1, 1, 1)
    glVertex3f(1, -1, 1)
    glVertex3f(1, -1, -1)
    glEnd()  # End of drawing color-cube


def pyramid(angle):
    glRotate(angle, True, True, True)
    glBegin(GL_QUADS)  # Begin drawing the pyramid with 4 triangles
    # Bottom face (y = -11)
    glColor3f(1, 1, 0)  # Yellow
    glVertex3f(1, -1, -1)
    glVertex3f(-1, -1, -1)
    glVertex3f(-1, -1, 1)
    glVertex3f(1, -1, 1)
    glEnd()
    glBegin(GL_TRIANGLES)
    # Front
    glColor3f(1, 0, 0)  # Red
    glVertex3f(0, 1, 0)
    glVertex3f(-1, -1, 1)
    glVertex3f(1, -1, 1)
    # Right
    glColor3f(0, 1, 0)  # Green
    glVertex3f(0, 1, 0)
    glVertex3f(1, -1, 1)
    glVertex3f(1, -1, -1)
    # Back
    glColor3f(0, 0, 1)  # Blue
    glVertex3f(0, 1, 0)
    glVertex3f(1, -1, -1)
    glVertex3f(-1, -1, -1)
    # Left
    glColor3f(1, 0, 1)  # Magenta
    glVertex3f(0, 1, 0)
    glVertex3f(-1, -1, -1)
    glVertex3f(-1, -1, 1)
    glEnd()  # Done drawing the pyramid


def main():
    initGL("3D")
    clock = pygame.time.Clock()

    glTranslatef(0, 0, -10)

    cubeAngle = 0;
    pyramidAngle = 0;

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glClearColor(1, 1, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # Clear color and depth buffers
        glPushMatrix()
        glTranslatef(2, 0, 0)
        cube(cubeAngle)
        cubeAngle -= 1.1
        glPopMatrix()
        glPushMatrix()
        glTranslatef(-2, 0, 0)
        pyramid(pyramidAngle)
        pyramidAngle += 1
        glPopMatrix()
        glRotate(1, True, True, True)
        pygame.display.flip()
        clock.tick(30)

main()