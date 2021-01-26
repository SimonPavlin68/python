import pygame, math, sys

BLACK = (0, 0, 0)
RED = (255, 0, 0)

class Boat:

    def __init__(self, coordinates, horizontal):
        self.submerged = False
        self.coordinates = coordinates
        self.horizontal = horizontal

    def hit(self, screen, STEP, coord):
        if not self.submerged:
            nothit = False
            for c in self.coordinates:
                if(c[0] == coord[0] and c[1] == coord[1]):
                    #print('bum')
                    c[2] = 1
                    pygame.draw.rect(screen, RED, [c[0] * STEP, c[1] * STEP, STEP, STEP])
                    pygame.display.update()
                    pygame.mixer.init()
                    sound = pygame.mixer.Sound("../pygame/audio/Flashbang.wav")
                    sound.play()
                if(c[2]) == 0:
                    nothit = True
            if(not nothit):
                self.submerged = True
                print('submerged')
                print(self.coordinates[0][0], self.coordinates[0][1])
                if(self.horizontal):
                    pygame.draw.rect(screen, BLACK, [self.coordinates[0][0]*STEP, self.coordinates[0][1]*STEP, STEP*len(self.coordinates), STEP], 2)
                else:
                    pygame.draw.rect(screen, BLACK, [self.coordinates[0][0]*STEP, self.coordinates[0][1]*STEP, STEP, STEP*len(self.coordinates)], 2)
                pygame.display.update()
                return True
            else:
                return False

    def submerged(self):
        return self.submerged

    def print(self):
        return self.submerged, self.coordinates