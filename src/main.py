import pygame
from helpers import *
from Config import *
from colors import *
from models.Game import Game

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

# Listsddd
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

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                Game.quit()
                exit()
    Game()
