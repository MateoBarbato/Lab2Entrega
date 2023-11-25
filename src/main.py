import pygame
from helpers import *
from Config import *
from colors import *
from models.Game import Game
from models.Level import Level
from dataLevels import level_map1
pygame.init()

while True:
    screen = createScreen()
    clock = pygame.time.Clock()
    muteState = MUTESTATE
    runMainMenu = True
    levelSelected = ''
    levelMap = None
    isRunning = True
    if runMainMenu:
        muteState, runMainMenu = mainMenu(screen, muteState)
    if runMainMenu == False:
        runMainMenu, levelSelected = levelSelector(screen, muteState)
        if levelSelected == 'level1':
            print('entre aca')
            levelMap = level_map1
        elif levelSelected == 'level2':
            print('en construccion...')
            levelMap = level_map1

    levelCanvas = Level(levelMap,
                        BACKGROUNDLEVEL1, screen)

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
            isRunning = False

        pygame.display.update()
        clock.tick(60)
