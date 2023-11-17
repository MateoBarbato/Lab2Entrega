import pygame
from helpers import *
from Config import *
from colors import *
from models.Bugs import Bug
from models.Game import Game
from models.Player import Player

pygame.init()
# Timers
# Flags
menu = 'main'
# muteState = False
muteState = MUTESTATE
powerUp1 = False
cheatOn = False
moveBugs = None
createBug = False

# Lists
bugs = []

# Timed events
moveBugInterval = 650
moveBugEvent = pygame.USEREVENT+1
createBugInterval = 2500
createBugEvent = pygame.USEREVENT+2

# Loading assets

playerImg = loadImage('totodyle.png')


try:
    screen = pygame.display.set_mode(SCREENSIZE)
    screen.fill(WHITE, pygame.Rect(0, 0, SCREENWIDTH, SCREENHEIGHT))
    pygame.display.set_caption("PokeBug")
    pygame.display.set_icon(loadImage('totodyle.png'))
except pygame.error as e:
    errMsg(e)

while True:

    # moveBugs = False
    # pygame.time.set_timer(moveBugEvent, moveBugInterval)
    # pygame.time.set_timer(createBugEvent, createBugInterval)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                Game.quit()
                exit()
    #         if event.key == pygame.K_SPACE:
    #             bug = None
    #             pass
    #         if event.key == pygame.K_h:
    #             hardcoreMode = not hardcoreMode
    #         if event.key == pygame.K_m:
    #             muteState = not muteState
    #         if event.key == pygame.K_SEMICOLON:
    #             cheatOn = not cheatOn
    #         if event.key == pygame.K_k:
    #             pass
    #     if event.type == pygame.USEREVENT+1:
    #         moveBugs = True
    #     if event.type == pygame.USEREVENT+2:
    #         createBug = True
    # if cheatOn:
    #     powerUp1 = True
    # else:
    #     powerUp1 = False

    Game()
