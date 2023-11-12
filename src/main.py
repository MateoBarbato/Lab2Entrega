import pygame
from helpers import errMsg,waitUser,waitUserClick
from Config import *
from colors import *
from models.Button import Button

# Flags
menu = 'main'
gameRunning = False
muteState = False

pygame.init()
clock = pygame.time.Clock()
clock.tick(60)

try :
    screen = pygame.display.set_mode(SCREENSIZE)
    pygame.display.set_caption("PokeBug")
except pygame.error as e:
    errMsg(e)

screenBackroundRect = pygame.Rect(0,0,SCREENWIDTH,SCREENHEIGHT)
screen.fill(BLACK,screenBackroundRect)
while True:
   muteState = waitUserClick(screen,muteState)

# MENU DE OPCIONES


    # while gameRunning:
    #     break
    # break

print('assd')