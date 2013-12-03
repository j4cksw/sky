
#Main Game Class.
import pygame
from pygame.locals import *
from game import *
from state.game_stage_001 import *
from state.game_state_menu import *
from state.intro import *
from state.gameover import *
from state.game_state_ending import *
from state.game_state_settings import *
from sys import exit
from configobj import ConfigObj


def main():
    pygame.init()
    config = ConfigObj("game.cfg")
    #Get screen settings
    #if config['screen']['fullscreen'] == "True":
    if config.as_bool('fullscreen'):
        screen = pygame.display.set_mode((1024, 768), FULLSCREEN )
    else:
        screen = pygame.display.set_mode((1024, 768), HWSURFACE,32 )
    #Set caption.
    pygame.display.set_caption("Skyscrapers Attack")
    nextstate = 0
    while True:
        if nextstate == 0:
            game = game_state_intro()
        elif nextstate == 1:
            game = game_state_menu()
        elif nextstate == 2:
            game = game_state_gameover()
        elif nextstate == 3:
            game = game_state_ending()
        elif nextstate == 4:
            game = game_stage_001()
        elif nextstate == 5:
            game = game_state_settings(config)
        else:
            exit()
        nextstate = game.vMain(screen)
        del game
        

main()