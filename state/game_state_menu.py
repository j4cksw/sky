import pygame
from pygame.locals import *
class game_state_menu():
    def __init__(self):
        self.background = pygame.image.load("data\image\\background\menu.png")
        self.clock = pygame.time.Clock()
        self.state = ""
        self.timer = 0
            
    def vProcess(self):
        self.clock.tick(30)
        self.timer += 1
        for event in pygame.event.get():
            if event.type == KEYUP:
                if event.key == K_q:
                    exit()
                if event.key == K_o:
                    self.state = "OPTIONS"
                else:
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
                return 4
            elif self.state == "OPTIONS":
                keepGoing = False
                return 5
            self.vRender(_screen)
            

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((1024, 768),HWSURFACE,32)
    pygame.display.set_caption("Test menu state")
    game = game_state_menu()
    game.vMain(screen)
    