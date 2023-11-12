import pygame
from helpers import *
from Config import *
from colors import *

# Loading assets



# Flags
menu = 'main'
gameRunning = False
muteState = False

pygame.init()
clock = pygame.time.Clock()
clock.tick(60)

try :
    screen = pygame.display.set_mode(SCREENSIZE)
    screen.fill(WHITE,pygame.Rect(0,0,SCREENWIDTH,SCREENHEIGHT))
    pygame.display.set_caption("PokeBug")
    drawBackground(screen,'fondo.png')
except pygame.error as e:
    errMsg(e)
# cleanScreen(screen)

while True:
    

   muteState = mainMenu(screen,muteState)

    # while gameRunning:
    #     break

