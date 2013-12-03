import pygame
from bullet import *

class Boss1(pygame.sprite.Sprite):


    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        
    def vInit(self):
        self.Enable = True
        self.vLoadImage()
        
        self.fPos_x = 1100
        self.fPos_y = 625
        self.fMoveSpeed = 5
        
        self.state = "MOVE_LEFT"
        self.image = self.imageList[0]
        self.rect = self.image.get_rect()
        self.rect.center = (self.fPos_x, self.fPos_y)
        self.frame = 0
        self.delay = 3
        self.pause = 0
        
        self.life = 1000
        self.ammo = 6
        self.bullet = [ Bullet(),Bullet(),Bullet(),Bullet(),Bullet(),Bullet()]
        self.timer = 0
    
    def vProcess(self, pBall = None, pShip = None):
        if self.Enable == False:
            return
        
        if self.state == "MOVE_LEFT":
            self.vMoveLeft()
        elif self.state == "MOVE_RIGHT":
            self.vMoveRight()
        elif self.state == "IDLE":
            pass
        
        if self.fPos_x <= 0 :
            self.state = "MOVE_RIGHT"
        elif self.fPos_x >= 1024:
            self.state = "MOVE_LEFT"
        if self.ammo == 0:
            self.state = "IDLE"
            self.timer += 1
            #print self.timer
            if self.timer > 100 :
                self.ammo = 6
                self.timer = 0
                self.state = "MOVE_LEFT"
        
        for i in range(len(self.bullet)):
            self.bullet[i].vProcess()
            
        
        
        #Check the ball collision
        if pBall != None:
            if self.state != "DEAD_LEFT" or self.state != "DEAD_RIGHT":
                if self.rect.colliderect(pBall.rect):
                    if self.state == "MOVE_LEFT" or "SHOOT_LEFT":
                        self.state = "DEAD_LEFT"
                        self.life -= 10*pBall.fSpeedX
                    elif self.state == "MOVE_RIGHT" or "SHOOT_RIGHT":
                        self.state = "DEAD_LEFT"
                        self.life -= 10*pBall.fSpeedX
        
        #Check X axis if matches with the plyer's ship then fire his gun.
        if pShip != None:
            if self.fPos_x == pShip.fPos_x:
                if self.state == "MOVE_LEFT" and self.bullet > 0:
                    self.state = "SHOOT_LEFT"
                    self.bullet[self.ammo-1].vInit(self.rect[0],self.rect[1]+65,-1)
                    self.ammo -= 1
                    
                elif self.state == "MOVE_RIGHT" and self.bullet > 0:
                    self.state = "SHOOT_RIGHT"
                    self.bullet[self.ammo-1].vInit(self.rect[0]+self.rect[2],self.rect[1]+65,1)
                    self.ammo -= 1
    
    def vRender(self):
        if self.Enable == False:
            return
        
        for i in range(len(self.bullet)):
            self.bullet[i].vRender()
        
        if self.state == "IDLE" or self.state == "MOVE_LEFT":
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
        elif self.state == "MOVE_RIGHT" :
            self.pause += 1
            if self.pause > self.delay:
                    #reset pause and advance animation
                    self.pause = 0
                    self.frame += 1
                    if self.frame >= len(self.imageListR):
                        self.frame = 0
                        self.image = self.imageListR[self.frame]
                    else:
                        self.image = self.imageListR[self.frame]
        elif self.state == "SHOOT_LEFT":
            self.pause += 1
            if self.pause > self.delay:
                    #reset pause and advance animation
                    self.pause = 0
                    self.frame += 1
                    if self.frame >= len(self.imageShoot):
                        self.frame = 0
                        self.state = "MOVE_LEFT"
                        self.image = self.imageShoot[self.frame]
                    else:
                        self.image = self.imageShoot[self.frame]
        elif self.state == "SHOOT_RIGHT":
            self.pause += 1
            if self.pause > self.delay:
                    #reset pause and advance animation
                    self.pause = 0
                    self.frame += 1
                    if self.frame >= len(self.imageShootR):
                        self.frame = 0
                        self.state = "MOVE_RIGHT"
                        self.image = self.imageShootR[self.frame]
                    else:
                        self.image = self.imageShootR[self.frame]
        elif self.state == "DEAD_LEFT":
            self.pause += 1
            if self.pause > self.delay:
                    #reset pause and advance animation
                    self.pause = 0
                    self.frame += 1
                    if self.frame >= len(self.imageDead):
                        #self.frame = 0
                        self.state = "MOVE_LEFT"
                        #self.image = self.imageDead[self.frame]
                    else:
                        self.image = self.imageDead[self.frame]
        
        self.rect.center = (self.fPos_x, self.fPos_y)
    
    def vMoveLeft(self):
        if self.fPos_x <= 0 :
            return
        self.fPos_x -= self.fMoveSpeed
    
    def vMoveRight(self):
        if self.fPos_x >= 1024 :
            return
        self.fPos_x += self.fMoveSpeed
    
    def vDestroy(self):
        pass
    
    def vLoadImage(self):
        self.imageList = []
        for i in range(2):
            imgName = "data\image\\boss\\Boss1Walk_%d.png" % i
            tmpImage = pygame.image.load(imgName)
            tmpImage = tmpImage.convert_alpha()
            self.imageList.append(tmpImage)
        self.imageListR = []
        for i in range(2):
            imgName = "data\image\\boss\\Boss1WalkR_%d.png" % i
            tmpImage = pygame.image.load(imgName)
            tmpImage = tmpImage.convert_alpha()
            self.imageListR.append(tmpImage)
        self.imageShoot = []
        for i in range(1,5):
            imgName = "data\image\\boss\\Boss1Shoot_%d.png" % i
            tmpImage = pygame.image.load(imgName)
            tmpImage = tmpImage.convert_alpha()
            self.imageShoot.append(tmpImage)
        self.imageShootR = []
        for i in range(1,5):
            imgName = "data\image\\boss\\Boss1Shoot_%dR.png" % i
            tmpImage = pygame.image.load(imgName)
            tmpImage = tmpImage.convert_alpha()
            self.imageShootR.append(tmpImage)
        self.imageDead = []
        for i in range(1,10):
            imgName = "data\image\\boss\\Boss1Die_%d.png" % i
            tmpImage = pygame.image.load(imgName)
            tmpImage = tmpImage.convert_alpha()
            self.imageDead.append(tmpImage)
    
    def vLoadSound(self):
        pass
        
        