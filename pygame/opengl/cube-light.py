import pygame
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
            glColor3fv(colors[x])
            #glColor3fv(RED)
            #x += 1
            glVertex3fv(vertices[vertex])
    glEnd()

    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glColor(BLACK)
            glVertex3fv(vertices[vertex])
    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glPushMatrix()
    color = [1.0,0.,0.,1.]
    glMaterialfv(GL_FRONT,GL_DIFFUSE,color)
    glutSolidSphere(2,20,20)
    glPopMatrix()
    glutSwapBuffers()
    return


def main():
    pygame.init()
    pygame.display.set_mode((WIDTH, HEIGHT), DOUBLEBUF|OPENGL)
    pygame.display.set_caption("Cube rotate")

    gluPerspective(50, (WIDTH/HEIGHT), 0.1, 50.0)

    glTranslatef(0.0,0.0,-5)

    glEnable(GL_DEPTH_TEST)
    #glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_NORMALIZE)
    glLightfv(GL_LIGHT0, GL_POSITION, (0,0,1));
    #glEnable(GL_FOG)
    #glFogfv(GL_FOG_COLOR, BLUE)
    #glFogi(GL_FOG_MODE, GL_LINEAR)
    #glFogf(GL_FOG_DENSITY, 0.2)
    #glFogf(GL_FOG_START, 1.5)
    #glFogf(GL_FOG_END, 5.0)

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glRotatef(1, 1, 1, 1) # angle, x, y, z

        #x = glGetDoublev(GL_MODELVIEW_MATRIX)
        #print(x)

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        glClearColor(1.0, 1.0, 1.0, 1.0);
        cube()
        pygame.display.flip()
        clock.tick(60)

main()