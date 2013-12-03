#Test ball.py
import pygame
from pygame.locals import *
from sys import exit
from ball import *

pygame.init()

screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Dr.wily balls")

background = pygame.Surface(screen.get_size())
background.fill((0, 0x99, 0))
screen.blit(background, (0, 0))

m_oBall = Ball()
m_oBall.vInit()

clock = pygame.time.Clock()
allSprites = pygame.sprite.Group(m_oBall)

while True:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        if event.type == KEYDOWN :
            if event.key == K_q:
                exit()
            
    #print avatar.fPos_x
    m_oBall.vProcess()
    #print avatar.fPos_x
    m_oBall.vRender()
        
    allSprites.clear(screen,background)
    allSprites.draw(screen)
    
    pygame.display.flip()
