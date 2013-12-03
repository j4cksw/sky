#Ending
import pygame
from pygame.locals import *
class game_state_ending():
    def __init__(self):
        self.background = pygame.image.load("data\image\\background\ending.png")
        self.clock = pygame.time.Clock()
        self.state = ""
        self.timer = 0
        
    def vInit(self):
        pass
        
    def vProcess(self):
        self.clock.tick(30)
        self.timer += 1
        
        if self.timer > 60:
            self.state = "END"
        
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
    game = game_state_ending()
    game.vMain(screen)
        