import pygame
import os

class Block(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.Enable = False
        self.disableimage = pygame.image.load(os.path.abspath("data/image/blocks/disable.png")).convert_alpha()
        self.imageList = []
        self.image = self.disableimage
        self.rect = self.image.get_rect()
        self.state = "IDLE"
        self.frame = 0
        self.delay = 3
        self.pause = 0
        self.isEndAnimate = False

    def vInit(self, _posX, _posY, _imageList):
        self.Enable = True
        self.imageList = _imageList
        self.posX = _posX
        self.posY = _posY
        self.image = self.imageList[0]



        self.movestep = 10

        self.rect = self.image.get_rect()
        self.rect.center = (self.posX, self.posY)
        self.state = "IDLE"

    def vProcess(self):
        if self.Enable == False:
            return

    def vRender(self):
        if self.Enable == False:

            return

        self.pause += 1
        if self.pause > self.delay:
            #reset pause and advance animation
            self.pause = 0
            self.frame += 1
            if self.frame >= len(self.imageList):
                if self.state == "BREAK":
                    self.isEndAnimate = True
                self.frame = 0
                self.image = self.imageList[self.frame]
            else:
                self.image = self.imageList[self.frame]

        self.rect.center = (self.posX, self.posY)

    def isBallCollide(self, _pBall):
        if self.rect.colliderect(_pBall.rect):
            return True
        return False

    def isPointIntersec(self, _refX, _refY):
        if _refX > self.rect[0] and _refX < self.rect[0] + self.rect[2]:
            if _refY > self.rect[1] and _refY < self.rect[1] + self.rect[3]:
                return True
        else:
            return False

    def vMoveUp(self):
        if self.Enable:
            self.posY -= self.rect[3]

    def vMoveDown(self):
        if self.Enable:
            self.posY += self.rect[3]
