"""Space ship class"""
""" Create by Prayoch Rujira """

import pygame

class spaceShip(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
    
    def vInit(self):
        
        self.loadImage()
        self.fPos_x = 320
        self.fPos_y = 45
        self.image = self.imageIdle[0]
        self.rect = self.image.get_rect()
        self.rect.center = (self.fPos_x, self.fPos_y)
        self.frame = 0
        self.delay = 4
        self.pause = 0
        self.state = "IDLE"
        
        self.fMoveSpeed = 25
        
        self.lifepoint = 500
        self.energy = 20
        
    
    def vProcess(self, pBullet = None):
        if self.state == "DEAD":
            return
        if self.state == "IDLE":
            self.vIdle()
        
        if self.lifepoint <= 0 or self.energy < 0:
            self.state = "DEAD"
            
        #self.fPos_x += self.fMoveX
        if pBullet != None:
            for i in range(len(pBullet)):
                if pBullet[i].rect.colliderect(self.rect) and pBullet[i].Enable == True:
                    
                    pBullet[i].Enable = False
                    self.lifepoint -= 100
        
                
    
    def vRender(self, _screen):
        if self.state == "IDLE":
            self.pause += 1
            if self.pause > self.delay:
                    #reset pause and advance animation
                    self.pause = 0
                    self.frame += 1
                    if self.frame >= len(self.imageIdle):
                        self.frame = 0
                        self.image = self.imageIdle[self.frame]
                    else:
                        self.image = self.imageIdle[self.frame]
        if self.state == "DEAD":
            self.pause += 1
            if self.pause > self.delay:
                self.pause = 0
                self.frame += 1
                if self.frame >= len(self.imageDead):
                    self.frame = self.frame-1
                    self.image = self.imageDead[self.frame]
                else:
                    self.image = self.imageDead[self.frame]
        
        self.rect.center = (self.fPos_x, self.fPos_y)
        #pygame.sprite.RenderPlain((self)).draw(_screen)
    
    def vIdle(self):
        self.fMoveX = 0
        self.state = "IDLE"
        
    
    def vMoveLeft(self):
        if self.fPos_x <= 0 :
            return
        self.fPos_x -= self.fMoveSpeed
        
        
    def vMoveRight(self):
        #self.fMoveX = +1
        if self.fPos_x >= 1024:
            return
        self.fPos_x += self.fMoveSpeed
    
    def vMoveDown(self):
        self.fPos_y += self.fMoveSpeed
    
    def vSetPos(self, _fPosX, _fPosY):
        self.fPos_x = _fPosX
        self.fPos_y = _fPosY
    
    def fGetPos(self):
        return (self.fPos_x, self.fPos_y)
        
    def loadImage(self):
        self.imageIdle = []
        for i in range(4):
            imgName = "data\image\spaceship\ship_00%d.png" % i
            tmpImage = pygame.image.load(imgName)
            tmpImage = tmpImage.convert_alpha()
            self.imageIdle.append(tmpImage)
        #Load dead image
        self.imageDead = []
        for i in range(7):
            imgName = "data\image\spaceship\die00%d.png" %i
            tmpImage = pygame.image.load(imgName).convert_alpha()
            self.imageDead.append(tmpImage)
    
    def vLoadSound(self):
        pass
    
    def bIsPointIntersec(self, _refX, _refY):
        if _refX >= self.rect[0] and _refX <= self.rect[0] + self.rect[2]:
            if _refY >= self.rect[1] and _refY <= self.rect[1] + self.rect[3]:
                return True
        else:
            return False
        