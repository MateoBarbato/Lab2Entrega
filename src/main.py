import pygame
from helpers import *
from Config import *
from colors import *
from models.Game import Game
from models.Level import Level
from dataLevels import level_map1, level_map2, level_map3
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
best5Scores = None
while True:
    data = loadDb()

    if runMainMenu:
        muteState = mainMenu(screen, muteState)
        runMainMenu = False
    if runMainMenu == False and levelScreen == True:
        runMainMenu, levelSelected = levelSelector(screen, muteState)
        isRunning = True
    if levelSelected == 0:
        isRunning = False
    else:
        if levelSelected == 1:
            print('entre aca')
            levelMap = level_map1
            backgroundMain = BACKGROUNDLEVEL1
            best5Scores = data['Level 1']
        elif levelSelected == 2:
            print('en construccion...')
            levelMap = level_map2
            backgroundMain = BACKGROUNDLEVEL2
            best5Scores = data['Level 2']
        elif levelSelected == 3:
            print('en construccion...')
            levelMap = level_map3
            backgroundMain = BACKGROUNDLEVEL3
            best5Scores = data['Level 3']

        levelCanvas = Level(levelMap,
                            backgroundMain, screen, muteState)

    while isRunning:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit()
                if event.key == pygame.K_p:
                    Pause(screen, levelCanvas)

        if levelCanvas.levelDone == False:
            levelCanvas.run()
        else:
            # TERMINO EL NIVEL
            # CREAR PANTALLA POST LEVEL
            lastScore = levelCanvas.scoreTotal
            isRunning = False
        pygame.display.update()
        clock.tick(60)
    # if levelSelected != 0 and levelCanvas.levelDone == True:
    #     levelCanvas.resetCounter()

    if levelSelected != 0:
        del levelCanvas
        newData5Top = saveScores(data, lastScore, levelSelected)

        isRunning, levelSelected = levelFinished(
            screen, BACKGROUNSEANIGHT, levelSelected, lastScore, newData5Top)

    if levelSelected == 0:
        levelScreen = True
    else:

        runMainMenu = False
        levelScreen = False
