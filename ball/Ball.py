"""Ball class"""
""" Create by Prayoch Rujira """

import pygame
import os

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)


    def vInit(self):
        self.LoadImage()
        self.Enable = True
        self.fPos_x = 300
        self.fPos_y = 95
        self.fSpeedX = 9
        self.fSpeedY = 9
        self.maxspeed = 20
        self.minspeed = 10

        self.image = self.imageList[0]
        self.rect = self.image.get_rect()

        self.rect.center = (self.fPos_x, self.fPos_y)
        self.frame = 0
        self.delay = 3
        self.pause = 0

        self.state = 'idele'
        self.iMoveX = 0;
        self.iMoveY = 0;

        self.iDirectX = 1;
        self.iDirectY = 1;

    def vChangeDirX(self):
        self.iDirectX = -self.iDirectX

    def vChangeDirY(self):
        self.iDirectY = -self.iDirectY

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
        self.fPos_x = self.fPos_x + round(self.fSpeedX * self.iDirectX)

    def vMoveY(self):
        self.fPos_y = self.fPos_y + round(self.fSpeedY * self.iDirectY)

    def bIsTouchCeiling(self):
        if self.fPoint_UP[1] <= 0:
            return True
        else:
            return False

    def vProcess(self, pShip = None, pBoss = None, pBlockMgr = None):
        bool = False
        if self.Enable == False:
            return bool
##        print self.rect
##        print self.fPos_x," ",self.fPos_y
        self.vUpdatePoint()
        ##Chect collision of the ball with border
        self.bBorderDetect(1024, 717)
##        if self.fPoint_BOTTOM[1] >= 717 and self.fPoint_LEFT[0] <= 0:
##            self.vChangeDirX()
##            self.vChangeDirY()
##        elif self.fPoint_BOTTOM[1] >= 717 and self.fPoint_RIGHT[0] >= 1024:
##            self.vChangeDirX()
##            self.vChangeDirY()
##        elif self.fPoint_UP[1] <= 0 and self.fPoint_LEFT[0] <= 0:
##            self.vChangeDirX()
##            self.vChangeDirY()
##        elif self.fPoint_UP[1] <= 0 and self.fPoint_RIGHT[0] >= 1024:
##            self.vChangeDirX()
##            self.vChangeDirY()
##        elif self.fPoint_RIGHT[0] >= 1024:
##            self.vChangeDirX()
##        elif self.fPoint_LEFT[0] < 0:
##            self.vChangeDirX()
##        elif self.fPoint_UP[1] < 0:
##
##            self.Enable = False
##        elif self.fPoint_BOTTOM[1] >= 717 and self.fPoint_BOTTOM[0] >= -10 and self.fPoint_BOTTOM[0] <= 1030:
##            self.vChangeDirY()

        ##Check collision of the ball with space ship
        if pShip != None:
            #print pShip.rect[0]," ",pShip.rect[1]
            if pShip.bIsPointIntersec(self.fPoint_UP[0], self.fPoint_UP[1]):
                if not pShip.bIsPointIntersec(self.fPoint_LEFT[0], self.fPoint_LEFT[1]) and not pShip.bIsPointIntersec(self.fPoint_RIGHT[0], self.fPoint_RIGHT[1]):
                    self.vChangeDirY()
                    if self.fSpeedX < self.maxspeed:
                        self.fSpeedX += 0.5
                        self.fSpeedY += 0.5

        ##Check collision withan enemy sprites
        if pBoss != None:
            if self.rect.colliderect(pBoss.rect):
                #print pBoss.state
                if pBoss.state != "DEAD_LEFT" :
                    self.vChangeDirX()
                    self.vChangeDirY()
        ##Check collision with blocks
        if pBlockMgr != None:
            i = 0
            for i in range(len(pBlockMgr.blocks)):
                if pBlockMgr.blocks[i].Enable == False:
                    continue
                if self.iDirectY == 1:
                    if pBlockMgr.blocks[i].isPointIntersec(self.fPoint_BOTTOM[0],self.fPoint_BOTTOM[1]):
                        self.vChangeDirY()
                        bool = True
                    if pBlockMgr.blocks[i].isPointIntersec(self.fPoint_LEFT[0],self.fPoint_LEFT[1]):
                        self.vChangeDirX()
                        bool = True
                    if pBlockMgr.blocks[i].isPointIntersec(self.fPoint_RIGHT[0],self.fPoint_RIGHT[1]):
                        self.vChangeDirX()
                        bool = True
                elif self.iDirectY == -1:
                    if pBlockMgr.blocks[i].isPointIntersec(self.fPoint_UP[0],self.fPoint_UP[1]):
                        self.vChangeDirY()
                        bool = True
                    if pBlockMgr.blocks[i].isPointIntersec(self.fPoint_LEFT[0],self.fPoint_LEFT[1]):
                        self.vChangeDirX()
                        bool = True
                    if pBlockMgr.blocks[i].isPointIntersec(self.fPoint_RIGHT[0],self.fPoint_RIGHT[1]):
                        self.vChangeDirX()
                        bool = True
        self.vMoveX()
        self.vMoveY()
        return bool

    def vRender(self, _screen):
        if self.Enable == False:
            self.image = self.BlankImage;
            self.rect.center = (self.fPos_x, self.fPos_y)
            return
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

        self.rect.center = (self.fPos_x, self.fPos_y)
        #pygame.sprite.RenderPlain((self)).draw(_screen)

    def vSetPos(self, _fPosX, _fPosY):
        self.fPos_x = _fPosX
        self.fPos_y = _fPosY
        self.image = self.imageList[0]
        self.iDirectX = 1;
        self.iDirectY = 1;
        self.fSpeedX = self.minspeed
        self.fSpeedY = self.minspeed
        self.rect.center = (_fPosX, _fPosY)
        #self.vUpdatePoint()
        self.Enable = True

    def LoadImage(self):
        self.imageList = []
        for i in range(1):
            imgName = os.path.abspath("data/image/ball/ball_00%d.png" % i)
            tmpImage = pygame.image.load(imgName)
            tmpImage = tmpImage.convert_alpha()
            self.imageList.append(tmpImage)
        self.BlankImage = pygame.image.load(os.path.abspath("data/image/ball/disable.png"))

    def vLoadsound(self):
        pass

    def bIsPointIntersec(self, _refX, _refY):
        if _refX > self.rect[0] and _refX < self.rect[0] + self.rect[2]:
            if _refY > self.rect[1] and _refY < self.rect[1] + self.rect[3]:
                return True
        else:
            return False

    def bBorderDetect(self, _borderWidht, _borderHeight):
        ##Chect collision of the ball with border
        if self.fPoint_BOTTOM[1] >= _borderHeight and self.fPoint_LEFT[0] <= 0:
            self.vChangeDirX()
            self.vChangeDirY()
        elif self.fPoint_BOTTOM[1] >= _borderHeight and self.fPoint_RIGHT[0] >= _borderWidht:
            self.vChangeDirX()
            self.vChangeDirY()
##        elif self.fPoint_UP[1] <= 0 and self.fPoint_LEFT[0] <= 0:
##            self.vChangeDirX()
##            self.vChangeDirY()
##        elif self.fPoint_UP[1] <= 0 and self.fPoint_RIGHT[0] >= 1024:
##            self.vChangeDirX()
##            self.vChangeDirY()
        elif self.fPoint_RIGHT[0] >= _borderWidht:
            self.vChangeDirX()
        elif self.fPoint_LEFT[0] < 0:
            self.vChangeDirX()
        elif self.fPoint_UP[1] < 0:
            self.Enable = False
        elif self.fPoint_BOTTOM[1] >= _borderHeight and self.fPoint_BOTTOM[0] >= -10 and self.fPoint_BOTTOM[0] <= 1030:
            self.vChangeDirY()

if __name__ == "__main__":
    print "Hello world"
