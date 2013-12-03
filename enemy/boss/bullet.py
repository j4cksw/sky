#Bullet class for boss firing.
import pygame
class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.vLoadImage()
        self.image = self.disableimage
        self.rect = self.image.get_rect()
        
        self.frame = 0
        self.delay = 3
        self.pause = 0
        
        self.iDirectX = 1
        self.iDirectY = -1
        self.Enable = False
        
        self.posX = 0
        self.posY = 0
        self.fSpeedX = 15
        self.fSpeedY = 15
    def vInit(self, _posX, _posY, _dirX, ):
        self.iDirectX = _dirX
        self.posX = _posX
        self.posY = _posY
        self.Enable = True
    
    def vUpdatePoint(self):
##Update the ball factors.        
        self.fPoint_UP = [ self.rect[0]+(self.rect[2]/2), self.rect[1] ]
        self.fPoint_BOTTOM = [ self.rect[0]+(self.rect[2]/2), self.rect[1]+self.rect[3] ]
        self.fPoint_LEFT = [ self.rect[0], self.rect[1]+(self.rect[3]/2) ]
        self.fPoint_RIGHT = [self.rect[0]+self.rect[2], self.rect[1]+(self.rect[3]/2) ]
##        self.fPoint_UL = [self.rect[0], self.rect[1]]
##        self.fPoint_UR = [self.rect[0]+self.rect[2], self.rect[1]]
##        self.fPoint_DL = [self.rect[0],self.rect[1]+self.rect[3]]
##        self.fPoint_DR = [self.rect[0]+self.rect[2], self.rect[1]+self.rect[3]]
    
    def vMoveX(self):
        self.posX = self.posX + (self.fSpeedX * self.iDirectX)
    
    def vMoveY(self):
        self.posY = self.posY + (self.fSpeedY * self.iDirectY)
        
    def vChangeDirX(self):
        self.iDirectX = -self.iDirectX
    
    def vChangeDirY(self):
        self.iDirectY = -self.iDirectY
        
    def vProcess(self, pShip = None):
        if self.Enable == False:
            return
        
        
        self.vUpdatePoint()
        
        if self.fPoint_LEFT[0] < 0 and self.fPoint_UP[1] != 0:
            self.vChangeDirX()
        elif self.fPoint_RIGHT[0] > 1024 and self.fPoint_UP != 0:
            self.vChangeDirX()
        elif self.fPoint_UP <= 0:
            self.Enable = False
        
        self.vMoveX()
        self.vMoveY()
        
        
    def vRender(self):
        
        if self.Enable == False:
            self.image = self.disableimage
        else:
            self.pause += 1
            if self.pause > self.delay:
            #reset pause and advance animation
                self.pause = 0
                self.frame += 1
                if self.frame >= len(self.imageList):
                    
                    self.frame = 0
                    self.image = self.imageList[self.frame]
                else:
                    self.image = self.imageList[self.frame]
        self.rect.center = (self.posX, self.posY)
        
    def vLoadImage(self):
        self.imageList = []
        for i in range(1):
            imgname = "data\image\\boss\\bullet_00%d.png" %i
            tmpimage = pygame.image.load(imgname).convert_alpha()
            self.imageList.append(tmpimage)
        self.disableimage = pygame.image.load("data\image\\boss\\bullet_disable.png").convert_alpha()
        
    