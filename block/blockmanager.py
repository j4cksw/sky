import pygame,random
from blocks import *

def pRandom():
    return int(random.uniform(0,4))

class BlockManager():
    def __init__(self):
        self.blocks = []
        self.block_width = 50
        self.block_height = 25
        self.maxrows = 15
        self.vLoadImage()
        #Create Blocks
        for i in range(25*19):
            self.blocks.append(Block());
        
        self.allBlocks = pygame.sprite.Group(self.blocks)
        
    def vInit(self):
        init_posX = 65
        init_posY = 455
        for i in range(19):
            self.blocks[i].vInit(init_posX, init_posY, self.blockimage[pRandom()])
            self.blocks[i+19].vInit(init_posX, init_posY+self.block_height, self.blockimage[pRandom()])
            self.blocks[i+19*2].vInit(init_posX, init_posY+self.block_height*2, self.blockimage[pRandom()])
            self.blocks[i+19*3].vInit(init_posX, init_posY+self.block_height*3, self.blockimage[pRandom()])
            self.blocks[i+19*4].vInit(init_posX, init_posY+self.block_height*4, self.blockimage[pRandom()])
            self.blocks[i+19*5].vInit(init_posX, init_posY+self.block_height*5, self.blockimage[pRandom()])
            self.blocks[i+19*6].vInit(init_posX, init_posY+self.block_height*6, self.blockimage[pRandom()])
            self.blocks[i+19*7].vInit(init_posX, init_posY+self.block_height*7, self.blockimage[pRandom()])
            self.blocks[i+19*8].vInit(init_posX, init_posY+self.block_height*8, self.blockimage[pRandom()])
            self.blocks[i+19*9].vInit(init_posX, init_posY+self.block_height*9, self.blockimage[pRandom()])
            self.blocks[i+19*10].vInit(init_posX, init_posY+self.block_height*10, self.blockimage[pRandom()])
            init_posX += self.block_width
        self.currentrow = 11
            
            
        
    def vProcess(self, pBall = None):
        bool = False
        if pBall != None:
            for i in range(len(self.blocks)):
                if self.blocks[i].Enable == True:
                    if self.blocks[i].isBallCollide(pBall):
                        self.blocks[i].imageList = self.explodeimage
                        self.blocks[i].state = "BREAK"
                        bool = True
                if self.blocks[i].isEndAnimate and self.blocks[i].state == "BREAK":
                    self.blocks[i].imageList = self.disableimage
                    self.blocks[i].Enable = False
        return bool
    
    def vMoveUp(self):
        for i in range(len(self.blocks)):
            self.blocks[i].vMoveUp()
        if self.currentrow < self.maxrows:
            init_posX = 65;init_posY = 455
            for i in range(19):
                self.blocks[i+19*self.currentrow].vInit(init_posX, init_posY+self.block_height*10, self.blockimage[pRandom()])
                init_posX += self.block_width
            self.currentrow += 1
        
        
    
    def vRender(self):
        for i in range(len(self.blocks)):
            self.blocks[i].vRender()
        
    
    def vLoadImage(self):
        self.blockimage = []
        self.blockimage_red = []
        self.blockimage_yellow = []
        self.blockimage_blue = []
        self.explodeimage = []
        self.disableimage = []
        tmpimage = pygame.image.load("data\image\\blocks\disable.png").convert_alpha()
        self.disableimage.append(tmpimage)
        self.explodeimage.append(tmpimage)
        #Load common block figure
        tmpImage = pygame.image.load("data\image\\blocks\\block.png")
        tmpImage = tmpImage.convert_alpha()
        self.blockimage.append([tmpImage])
        tmpImage = pygame.image.load("data\image\\blocks\\block_red.png")
        tmpImage = tmpImage.convert_alpha()
        self.blockimage.append([tmpImage])
        tmpImage = pygame.image.load("data\image\\blocks\\block_yellow.png")
        tmpImage = tmpImage.convert_alpha()
        self.blockimage.append([tmpImage])
        tmpImage = pygame.image.load("data\image\\blocks\\block_blue.png")
        tmpImage = tmpImage.convert_alpha()
        self.blockimage.append([tmpImage])
        #Load figure of block when it's explode
        for i in range(3):
            imgname = "data\image\\blocks\\explode%d.png" % i
            tmpImage = pygame.image.load(imgname)
            tmpImage = tmpImage.convert_alpha()
            self.explodeimage.append(tmpImage)
        #Load disable images
        
        
    def bIsPointIntersec(self, _refX, _refY):
        for i in range(len(self.blocks)):
            if self.blocks[i].Enable:
                return self.blocks[i].isPointIntersec(_refX,_refY)
    
    def countEnableBlocks(self):
        count = 0;
        for i in range(len(self.blocks)):
            if self.blocks[i].Enable:
                count += 1
        return count