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

def circle(radius):
    points = [[radius * math.sin(math.radians(deg)), radius * math.cos(math.radians(deg)), 0.0] for deg in range(360)]
    glLineWidth(5)
    glBegin(GL_LINE_STRIP)
    glColor3fv(BLUE)
    for pt in points:
        glVertex(pt)
    glVertex(points[0]) # zaključek
    glEnd()


def main():
    pygame.init()
    pygame.display.set_mode((WIDTH, HEIGHT), DOUBLEBUF|OPENGL)
    pygame.display.set_caption("Polygon - circle")

    gluPerspective(50, (WIDTH/HEIGHT), 0.1, 50.0)

    glTranslatef(0.0,0.0,-5)

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glRotatef(1, 0, 1, 0) # angle, x, y, z

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        glClearColor(1.0, 1.0, 1.0, 1.0);
        circle(1)
        pygame.display.flip()
        clock.tick(60)

main()