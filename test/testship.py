#Test for spaceship
import pygame
from pygame.locals import *
from sys import exit
from spaceship import *

pygame.init()

screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Dr.wily spaces ship")

background = pygame.Surface(screen.get_size())
background.fill((0, 0x99, 0))
screen.blit(background, (0, 0))

avatar = spaceShip()
avatar.vInit()

clock = pygame.time.Clock()
allSprites = pygame.sprite.Group(avatar)
space_dir = "IDLE"
keepGoing = True
mouse_move = False
mouse_pos = avatar.fGetPos()

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
    
    screen.blit(background, (0, 0))
    #print avatar.fPos_x
    avatar.vProcess()
    #print avatar.fPos_x
    avatar.vRender(screen)
        
    #allSprites.clear(screen,background)
    #allSprites.draw(screen)
    
    pygame.display.flip()