#Menu settings
import pygame
from pygame.locals import *
from configobj import ConfigObj
#config = ConfigObj(filename)

class game_state_settings():
  
    
    def __init__(self, _config = None):
        self.background = pygame.image.load("data\image\\background\settings.jpg")
        self.font = pygame.font.Font("cpu.ttf", 36)
        self.config = _config
        self.updateList()
        self.sectionList = [
                            self.font.render("screen", True, (0, 255, 0)),
                            self.font.render("sound", True, (0, 255, 0)),
                            self.font.render("key", True, (0, 255, 0)),
                            ]
        self.commandList = [
                            self.font.render("Load default", True, (255, 0, 0)),
                            self.font.render("Exit", True, (255, 0, 0)),
                           ]
        self.clock = pygame.time.Clock()
        self.timer = 0
        self.currentItem = 0
        self.state = ""
        #print self.config['screen']['fullscreen']
    
    def vProcess(self):
        self.clock.tick(30)
        self.timer += 1
        self.updateList()
        for event in pygame.event.get():
            if event.type == KEYUP:
                if event.key == K_ESCAPE:
                    self.state = "END"
            if event.type == QUIT:
                exit()
                    
##                else:
##                    self.state = "END"
    
    def vRender(self, _screen):
        linex = 400
        liney = 50
        _screen.blit(self.background,(0,0))
        #Blit section
        for section in range(len(self.sectionList)):
            section_rect = self.sectionList[section].get_rect()
            section_rect.center = (linex, liney)
            liney += 36
            _screen.blit(self.sectionList[section], section_rect)
            
            #Blit it's options
            for list in range(len(self.optionList[section])):
                list_rect = self.optionList[section][list].get_rect()
                list_rect.center = (linex, liney)
                liney += 36
                _screen.blit(self.optionList[section][list], list_rect)
        
        #Blit settings command
        for command in range(len(self.commandList)):
            command_rect = self.commandList[command].get_rect()
            command_rect.center = (linex, liney)
            liney += 36
            _screen.blit(self.commandList[command], command_rect)
        pygame.display.flip()
    
    def vMain(self, _screen):
        keepGoing = True
        while keepGoing:
            self.vProcess()
            if self.state == "END":
                keepGoing = False
                return 1
            self.vRender(_screen)
    
    def updateList(self):
        screenOptions = [
                            self.font.render("Full screen : "+self.config['fullscreen'],True,(255,255,255))
                            ]

        soundOptions = [
                            self.font.render("Music volume : "+self.config['sound']['bgm'],True,(255,255,255)),
                            self.font.render("SFX volume : "+self.config['sound']['sfx'],True,(255,255,255)),
                            ]
        keySettings = [
                            self.font.render("Move left : "+ pygame.key.name(int(self.config['key']['move_left'])),True,(255,255,255)),
                            self.font.render("Move Right : "+ pygame.key.name(int(self.config['key']['move_right'])),True,(255,255,255)),
                            self.font.render("Action : "+ pygame.key.name(int(self.config['key']['action'])),True,(255,255,255)),
                            self.font.render("Get item : "+ pygame.key.name(int(self.config['key']['get_item'])),True,(255,255,255)),
                            self.font.render("Fire : "+ pygame.key.name(int(self.config['key']['fire'])),True,(255,255,255)),
                            ]
        self.optionList = [ screenOptions, soundOptions, keySettings ]
    

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((800, 600),HWSURFACE,32)
    pygame.display.set_caption("Test options state")
    game = game_state_settings(ConfigObj("game.cfg"))
    game.vMain(screen)