from textwrap import fill
import pygame
from helpers import *
from Config import *
from colors import *
from models.Player import Player

# Loading assets
try:
    playerImg = pygame.image.load('assets/totodyle.png')
except FileNotFoundError:
    errMsg('Error while loading files. Exiting the game...')
    exit()


# Flags
menu = 'main'
gameRunning = True
muteState = False
move_up = None
move_down = None

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

while True:
    

    muteState = mainMenu(screen,muteState)

    player = Player(playerImg,SCREENWIDTH/2,SCREENHEIGHT/2,50,50,screen)

    while gameRunning:
        cleanScreen(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    # limpiar()
                    gameRunning = False
                if event.key == pygame.K_SPACE:
                    pass
                if event.key == pygame.K_h:
                    hardcoreMode = not hardcoreMode
                if event.key == pygame.K_m:
                    muteState = not muteState
                if event.key == pygame.K_SEMICOLON:
                    cheatOn = not cheatOn
                if event.key == pygame.K_k:
                    pass

        player.blitPlayer()

        player.movePlayer(4)
        pygame.display.flip()
        

