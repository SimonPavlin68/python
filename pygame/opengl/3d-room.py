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


def room():
    glActiveTexture(GL_TEXTURE0)
    glEnable(GL_TEXTURE_2D)

    glPushMatrix()
    glBegin(GL_QUADS)

    glTexCoord2f(0, 0)
    glVertex3f(-1, -1, -1)
    glTexCoord2f(1, 0)
    glVertex3f(3, -1, -1)
    glTexCoord2f(1, 1)
    glVertex3f(3, 3, -1)
    glTexCoord2f(0, 1)
    glVertex3f(-1, 3, -1)
    glEnd()

    glDisable(GL_TEXTURE_2D)
    glActiveTexture(GL_TEXTURE1)
    glEnable(GL_TEXTURE_2D)
    #glBindTexture(GL_TEXTURE_2D, 1)

    glBegin(GL_QUADS)
    glTexCoord2f(0, 0)
    glVertex3f(-1, 3, 3)
    glTexCoord2f(1, 0)
    glVertex3f(-1, 3, -1)
    glTexCoord2f(1, 1)
    glVertex3f(-1, -1, -1)
    glTexCoord2f(0, 1)
    glVertex3f(-1, -1, 3)

    glEnd()
    glPopMatrix()


def main():
    pygame.init()
    pygame.display.set_mode((WIDTH, HEIGHT), DOUBLEBUF | OPENGL)
    pygame.display.set_caption("3D room")

    glEnable(GL_DEPTH_TEST)

    gluPerspective(50, (WIDTH / HEIGHT), 0.1, 50.0)

    glTranslatef(0.0, 0.0, -5)

    clock = pygame.time.Clock()

    img1 = pygame.image.load('brick.jpg')
    texture1 = pygame.image.tostring(img1, "RGB", 1)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, img1.get_width(), img1.get_height(), 0, GL_RGB, GL_UNSIGNED_BYTE, texture1)

    img2 = pygame.image.load('wood.jpg')
    texture2 = pygame.image.tostring(img2, "RGB", 1)
    id = glGenTextures(1)
    print(id)
    glBindTexture(GL_TEXTURE_2D, id)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, img2.get_width(), img2.get_height(), 1, GL_RGB, GL_UNSIGNED_BYTE, texture2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glClearColor(1, 1, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # Clear color and depth buffers

        room()

        #glRotate(1, True, True, True)
        pygame.display.flip()
        clock.tick(60)

main()