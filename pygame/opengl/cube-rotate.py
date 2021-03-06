import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

WIDTH = 800
HEIGHT = 600

BLACK = (0, 0, 0)
RED = (1, 0, 0)
GREEN = (0, 1, 0)
BLUE = (0, 0, 1)
WHITE = (1, 1, 1)

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
    BLUE,
    GREEN,
    RED,
    BLUE,
    GREEN,
    RED
    )
krneki = (
    (0,0),
    (0,1),
    (1,1),
    (1,0)
)

def cube():
    glBegin(GL_QUADS)
    #x = 0
    for surface in surfaces:
        #glColor3fv(colors[x])
        #x += 1
        #glColor3fv(RED)
        i = 0
        for vertex in surface:
            glTexCoord2f(krneki[i][0], krneki[i][1])
            i+=1
            glVertex3fv(vertices[vertex])
    glEnd()

    #glBegin(GL_LINES)
    #for edge in edges:
    #    for vertex in edge:
    #        glColor(BLACK)
    #        glVertex3fv(vertices[vertex])
    #glEnd()


def main():
    pygame.init()
    pygame.display.set_mode((WIDTH, HEIGHT), DOUBLEBUF|OPENGL)
    pygame.display.set_caption("Cube rotate")

    glEnable(GL_DEPTH_TEST)

    gluPerspective(50, (WIDTH/HEIGHT), 0.1, 50.0)

    glTranslatef(0.0,0.0,-5)

    clock = pygame.time.Clock()

    img = pygame.image.load('wood.jpg')
    textureData = pygame.image.tostring(img, "RGB", 1)

    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, img.get_width(), img.get_height(), 0, GL_RGB, GL_UNSIGNED_BYTE, textureData)
    glEnable(GL_TEXTURE_2D)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glRotatef(1, 1, 0.1, 1) # angle, x, y, z

        #x = glGetDoublev(GL_MODELVIEW_MATRIX)
        #print(x)

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        glClearColor(1.0, 1.0, 1.0, 1.0)
        cube()
        pygame.display.flip()
        clock.tick(60)

main()