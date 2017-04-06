import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *


def main():
    pygame.init()
    pygame.display.set_mode((600,600), DOUBLEBUF|OPENGL)
main()

img = pygame.image.load('wood.jpg')
textureData = pygame.image.tostring(img, "RGB", 1)

glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, img.get_width(), img.get_height(), 0, GL_RGB, GL_UNSIGNED_BYTE, textureData)
glEnable(GL_TEXTURE_2D)

gluPerspective(50, 1, 0.1, 70)
#glTranslatef(0,0,-5)

#gluLookAt(eyeX, eyeY, eyeZ, centerX, centerY, centerZ, upX, upY, upZ)
gluLookAt(0, 0, 5, 0, 0, -5, 0, 2, 0)

def wall():
    glBegin(GL_QUADS)
    glTexCoord2f(0,0)
    glVertex3f(-1,-1,2)
    glTexCoord2f(0,1)
    glVertex3f(-1,1,2)
    glTexCoord2f(1,1)
    glVertex3f(1,1,-2)
    glTexCoord2f(1,0)
    glVertex3f(1,-1,-2)
    glEnd()


def drawground():
    glPushMatrix()

    glTranslate(-1, -1, -1)
    glRotate(90, True, False, False)

    glBegin(GL_QUADS)
    glColor(0.6, 0.6, 0.6)
    glVertex(0, 0)
    glVertex(0, 300)
    glVertex(300, 300)
    glVertex(300, 0)
    glEnd()

    glPopMatrix()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()


    #glRotatef(1, 0, 0, 1)  # angle, x, y, z
    #glRotate(1, False, False, True)

    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glClearColor(1.0, 1.0, 1.0, 1.0);

    wall()
    #drawground()

    pygame.display.flip()
    pygame.time.wait(50)