import pygame
from helpers import errMsg,waitUser,waitUserClick
from Config import *
from colors import (BLACK)


# Flags
menu = 'main'
gameRunning = False

pygame.init()


try :
    screen = pygame.display.set_mode(SCREENSIZE, 0)
    pygame.display.set_caption("PokeBug")
except pygame.error as e:
    errMsg(e)

screenBackroundRect = pygame.Rect(0,0,SCREENWIDTH,SCREENHEIGHT)
screen.fill(BLACK,screenBackroundRect)
while True:
    waitUserClick()
# MENU DE OPCIONES


    while gameRunning:
        break
    break

print('assd')