#Intro state.
import pygame
from pygame.locals import *
import os
class game_state_intro():
    def __init__(self):
        self.background = pygame.image.load(os.path.abspath("data/image/background/intro.png"))
        self.clock = pygame.time.Clock()
        self.state = ""
        self.timer = 0


    def vProcess(self):
        self.clock.tick(30)
        self.timer += 1

        if self.timer > 60:
            self.state = "END"
        for event in pygame.event.get():
            pass

    def vRender(self, _screen):
        _screen.blit(self.background,(0,0))
        pygame.display.flip()

    def vMain(self, _screen):
        keepGoing = True
        while keepGoing:
            self.vProcess()
            if self.state == "END":
                keepGoing = False
                return 1
            self.vRender(_screen)


if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((1024, 768),HWSURFACE,32)
    pygame.display.set_caption("Test intro state")
    game = game_state_intro()
