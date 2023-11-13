import pygame
from helpers import *
from Config import *
from colors import *
from models.Bugs import Bug
from models.Player import Player

pygame.init()
clock = pygame.time.Clock()
clock.tick(60)

# Timers 
# Flags
menu = 'main'
gameRunning = True
muteState = False
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
try:
    playerImg = pygame.image.load('assets/totodyle.png')
    bugImg = pygame.image.load('assets/bug.png')
except FileNotFoundError:
    errMsg('Error while loading files. Exiting the game...')
    exit()
background = loadBackground('fondo.png')

try :
    screen = pygame.display.set_mode(SCREENSIZE)
    screen.fill(WHITE,pygame.Rect(0,0,SCREENWIDTH,SCREENHEIGHT))
    pygame.display.set_caption("PokeBug")
except pygame.error as e:
    errMsg(e)

while True:
    player = Player(playerImg,SCREENWIDTH/2,SCREENHEIGHT/2,50,50,screen)
    bugs.append(Bug(bugImg,randIntPos('x',60),randIntPos('y',60),60,60,screen))
    # bug = Bug(bugImg,randIntPos('x'),randIntPos('y'),60,60,screen)
    muteState = mainMenu(screen,muteState)
    gameRunning = True
    moveBugs = False
    pygame.time.set_timer(moveBugEvent, moveBugInterval)
    pygame.time.set_timer(createBugEvent, createBugInterval)
    while gameRunning:  
        # BLIT ZONE
        drawBackground(screen,background)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    # limpiar()
                    gameRunning = False
                if event.key == pygame.K_SPACE:
                    bug = None
                    pass
                if event.key == pygame.K_h:
                    hardcoreMode = not hardcoreMode
                if event.key == pygame.K_m:
                    muteState = not muteState
                if event.key == pygame.K_SEMICOLON:
                    cheatOn = not cheatOn
                if event.key == pygame.K_k:
                    pass
            if event.type == pygame.USEREVENT+1:
                moveBugs = True
            if event.type == pygame.USEREVENT+2:
                createBug = True
        if cheatOn:
            powerUp1 = True
        else:
            powerUp1 = False

        if player:
            player.blitPlayer()
            if powerUp1:
                player.movePlayer(8)
            else:
                player.movePlayer(4)
        
        if createBug:
            if len(bugs) < 8:
                print(len(bugs))
                bugs.append(Bug(bugImg,randIntPos('x',60),randIntPos('y',60),60,60,screen))
            createBug=False

        for bug in bugs[:]:
            if moveBugs:
                bug.moveRandom(25)
            bug.blitBug()
        moveBugs=False
  

        # "Gravity"
        # if player.rect.bottom < SCREENHEIGHT:
        #     if player.speedY == 0:
        #         player.rect.move_ip(0,3)


        

        pygame.display.flip()
        

