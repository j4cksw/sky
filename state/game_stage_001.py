import pygame
from pygame.locals import *
from sys import exit
from spaceship.spaceship import *
from ball.Ball import *
from enemy.boss.boss1 import *
from block.blockmanager import BlockManager


class game_stage_001():
    def __init__(self):
        pass
    
    
    
    def vInit(self):
        
        self.state = "INIT"
        pygame.mixer.init()
        pygame.mixer.music.load("data\\bgm\cutman.mp3")
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1, 0.0)
        
        self.background = pygame.image.load("data\image\\background\stage1.png")
        #Init objects
        self.ship = spaceShip()
        self.ship.vInit()
        self.ball = Ball()
        self.ball.vInit()
        self.ball.Enable = False
        self.boss = Boss1()
        self.boss.vInit()
        self.boss.Enable = False
        self.BlockMgr = BlockManager()
        self.BlockMgr.vInit()
        #init clock
        self.clock = pygame.time.Clock()
        #group sprites
        #self.allSprites = pygame.sprite.Group(self.ship, self.boss, self.ball, self.BlockMgr.blocks, self.boss.bullet)
        self.allSprites = pygame.sprite.Group(self.ship, self.ball, self.BlockMgr.blocks, self.boss.bullet)

        self.space_dir = "IDLE"
        
        self.mouse_move = False
        self.mouse_pos = self.ship.fGetPos()
        self.timer = 0
        #load font
        self.centerFont = pygame.font.Font("data/font/cpu.ttf", 36)
        self.bigfont = pygame.font.Font("data/font/cpu.ttf", 120)
        #center message
        self.msg = ""
        self.Message = self.bigfont.render("GET READY!!",True,( 255, 255, 255))
        self.Message_rect = self.Message.get_rect()
        self.Message_rect.center = (0,382)
        self.state = "RUNNING"
        #init score
        self.score = 0
        #Load BGM"
        
    
    def vProcess(self):
        
        self.clock.tick(30)
        #print pygame.time.get_ticks()
        self.text_surface = self.centerFont.render("SCORE : %15d" %self.score, True, (255,255,255))
        en = self.ship.energy
        if en < 0:
            en = 0
        self.energy_text = self.centerFont.render("ENERGY :  %d" %self.ship.energy, True, (255,255,255)) 
        
        #Tick the timer
        self.timer += 1
        ##print self.timer
        if self.Message_rect.center[0] <= 512:
            self.Message_rect.center = (self.Message_rect.center[0]+18,  self.Message_rect.center[1])
        if self.timer >= 120 :
            if self.Message_rect[0] < 1024:
                if self.msg == "GAME OVER":
                    self.state = "GAME_OVER"
                    return
                elif self.msg == "YOU WIN":
                    self.state = "END"
                    return
                self.Message_rect.center = (self.Message_rect.center[0]+18,  self.Message_rect.center[1])
                
        
        if self.ship.state == "DEAD" and self.ship.frame == len(self.ship.imageDead)-1:
            self.msg = "GAME OVER"    
            self.Message = self.bigfont.render("",True,( 255, 255, 255))
            self.Message_rect.center = (512, 382)
 
        if self.boss.life <= 0 and self.boss.state == "DEAD_LEFT":
            self.msg = "YOU WIN"
            self.Message = self.bigfont.render("",True,( 255, 255, 255))
            self.Message_rect.center = (512, 382)
            
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            if event.type == KEYDOWN :
                #print pygame.key.name(275)    
                if event.key == 276:
                    self.space_dir = "LEFT"
                    self.mouse_move = False
                elif event.key == 275:
                    self.space_dir = "RIGHT"
                    self.mouse_move = False
                
                elif event.key == K_SPACE:
                    if self.ball.Enable == False:
                        self.ship.energy -= 1
                        #self.ball.Enable = True
                        self.ball.vSetPos(self.ship.rect[0]+(self.ship.rect[2]/2), self.ship.rect[1]+self.ship.rect[3]+(self.ship.rect[3]/2))
##                elif event.key == K_UP:
##                    self.BlockMgr.vMoveUp()
            elif event.type == KEYUP:
                    self.space_dir = "IDLE"
                    if event.key == K_q:
                        self.state = "QUIT"
                        return
            elif event.type == MOUSEMOTION:
                self.mouse_pos = event.pos
                self.mouse_move = True
            elif event.type == MOUSEBUTTONDOWN:
                if self.ball.Enable == False:
                    self.ship.energy -= 1
                    #self.ball.Enable = True
                    self.ball.vSetPos(self.ship.rect[0]+(self.ship.rect[2]/2), self.ship.rect[1]+self.ship.rect[3]+(self.ship.rect[3]/2))
            else:
                self.space_dir = "IDLE"
        
        #print self.ball.rect
        
        if self.space_dir == "LEFT" :
            self.ship.vMoveLeft()
        elif self.space_dir == "RIGHT":
            self.ship.vMoveRight()
        elif self.mouse_move == True:
            if self.mouse_pos[0] < self.ship.fGetPos()[0]:
                self.ship.vMoveLeft()
            if self.mouse_pos[0] > self.ship.fGetPos()[0]:
                self.ship.vMoveRight()
            if self.mouse_pos[0] == self.ship.fGetPos()[0]:
                self.mouse_move = False
                self.ship.vIdle()
        else:
            self.ship.vIdle()
        
        if self.BlockMgr.countEnableBlocks() < 20 or self.BlockMgr.currentrow >= 13:
            self.boss.Enable = True
        if self.BlockMgr.countEnableBlocks() < 100 and self.BlockMgr.currentrow !=self.BlockMgr.maxrows:
            self.BlockMgr.vMoveUp()
        
            
        self.ship.vProcess(self.boss.bullet)
        self.ball.vProcess(self.ship, self.boss, self.BlockMgr)
        #self.ball.vProcess(self.ship, self.boss)
        self.boss.vProcess(self.ball, self.ship)
        if self.BlockMgr.vProcess(self.ball):
            self.score += 100;
            #Chance to create item
        
        if self.ship.energy == 0 and not self.ball.Enable:
            self.ship.state = "DEAD"
        
        
        
        
    def vRender(self, _screen):
        self.ship.vRender(_screen)
        self.ball.vRender(_screen)
        self.boss.vRender()
        self.BlockMgr.vRender()
##        self.allSprites.clear(_screen, self.background)
##        self.allSprites.clear(_screen, self.text_surface)
        _screen.blit(self.background,(0,0))
        _screen.blit(self.text_surface,(790, 720))
        _screen.blit(self.energy_text,(10, 720))
        
        self.allSprites.draw(_screen)
        _screen.blit(self.boss.image, self.boss.rect)
        _screen.blit(self.Message, self.Message_rect)
        
       
        pygame.display.flip()
         
    
    def vDestroy(self):
        pass
        
    def vLoadBGM(self):
        pass
    
    def vMain(self, _screen):
        self.vInit()
        keepGoing = True
        while keepGoing:
            if self.state == "RUNNING":
                self.vProcess()
            elif self.state == "QUIT":
                keepGoing = False
                pygame.mixer.music.stop()
                return 1
            elif self.state == "GAME_OVER":
                keepGoing = False
                pygame.mixer.music.stop()
                return 2
            elif self.state == "END":
                keepGoing = False
                pygame.mixer.music.stop()
                return 3
            self.vRender(_screen)
            
                
##
if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((1024, 768), DOUBLEBUF | HWSURFACE, 32)
    pygame.display.set_caption("Skyscrapers Attack Demo")
    
    game = game_stage_001()
    game.vInit()
    screen.blit(game.background, (0, 0))
    keepGoing = True
    while keepGoing:
        
        #print game.state
        if game.state == "RUNNING":
            game.vProcess()
        elif game.state == "QUIT":
            keepGoing = False
        game.vRender(screen)
    