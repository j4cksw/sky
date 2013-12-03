#Test ship and ball
import pygame
from pygame.locals import *
from sys import exit
from spaceship import *
from ball import *
###INIT
pygame.init()

screen = pygame.display.set_mode((1024, 768))
pygame.display.set_caption("Dr.wily spaces ship and the ball")

background = pygame.Surface(screen.get_size())
background.fill((0, 0x99, 0))
screen.blit(background, (0, 0))

avatar = spaceShip()
avatar.vInit()
m_oBall = Ball()
m_oBall.vInit()

clock = pygame.time.Clock()
allSprites = pygame.sprite.Group(avatar, m_oBall)
#allSprites = pygame.sprite.Group(m_oBall)
space_dir = "IDLE"
keepGoing = True
mouse_move = False
mouse_pos = avatar.fGetPos()
###PROCESS
while True:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        if event.type == KEYDOWN :
            if event.key == K_LEFT:
                space_dir = "LEFT"
                mouse_move = False
            elif event.key == K_RIGHT:
                space_dir = "RIGHT"
                mouse_move = False
            elif event.key == K_q:
                exit()
            elif event.key == K_SPACE:
                if m_oBall.Enable == False:
                    m_oBall.vSetPos(avatar.rect[0]+(avatar.rect[2]/2), avatar.rect[1]+(avatar.rect[3])+(m_oBall.rect[3]/2))
        elif event.type == KEYUP:
            space_dir = "IDLE"
        elif event.type == MOUSEMOTION:
            mouse_pos = event.pos
            mouse_move = True
        else:
            space_dir = "IDLE"
    
    if space_dir == "LEFT" :
        avatar.vMoveLeft()
    elif space_dir == "RIGHT":
        avatar.vMoveRight()
    elif mouse_move == True:
        if mouse_pos[0] < avatar.fGetPos()[0]:
            avatar.vMoveLeft()
        if mouse_pos[0] > avatar.fGetPos()[0]:
            avatar.vMoveRight()
        if mouse_pos[0] == avatar.fGetPos()[0]:
            mouse_move = False
            avatar.vIdle()
    else:
        avatar.vIdle()
    
    #print avatar.fPos_x
    avatar.vProcess()
    m_oBall.vProcess(avatar)
###Render    
    #print avatar.fPos_x
        
    avatar.vRender(screen)
    m_oBall.vRender(screen)
       
    allSprites.clear(screen,background)
    allSprites.draw(screen)
    pygame.display.flip() 
    
############