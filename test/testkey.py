import pygame
from pygame.locals import *
import os
pygame.init()
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
                exit()
        if event.type == KEYDOWN :
            if event.key == K_ESCAPE:
                exit()
            print pygame.key.name(event.key)