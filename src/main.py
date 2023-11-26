import pygame
from helpers import *
from Config import *
from colors import *
from models.Game import Game
from models.Level import Level
from dataLevels import level_map1, level_map2
pygame.init()
screen = createScreen()
clock = pygame.time.Clock()
muteState = MUTESTATE
runMainMenu = True
levelSelected = ''
levelMap = None
isRunning = True
levelScreen = True
backgroundMain = BACKGROUNDLEVEL1
lastScore = 0
while True:
    print(levelSelected)
    if runMainMenu:
        muteState, runMainMenu = mainMenu(screen, muteState)
    if runMainMenu == False and levelScreen == True:
        runMainMenu, levelSelected = levelSelector(screen, muteState)
        isRunning = True
    if levelSelected == 1:
        print('entre aca')
        levelMap = level_map1
        backgroundMain = BACKGROUNDLEVEL1
    elif levelSelected == 2:
        print('en construccion...')
        levelMap = level_map2
        backgroundMain = BACKGROUNDLEVEL2

    levelCanvas = Level(levelMap,
                        backgroundMain, screen)

    while isRunning:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    Game.quit()
                    exit()

        if levelCanvas.levelDone == False:
            levelCanvas.run()
        else:
            # TERMINO EL NIVEL
            # CREAR PANTALLA POST LEVEL
            lastScore = levelCanvas.scoreTotal
            isRunning = False
            print(lastScore)
        pygame.display.update()
        clock.tick(60)
    isRunning, levelSelected = levelFinished(
        screen, BACKGROUNSEANIGHT, levelSelected, lastScore)
    if levelSelected == 0:
        runMainMenu = True
    else:
        runMainMenu = False
        levelScreen = False
