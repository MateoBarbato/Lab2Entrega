from ast import main
from json import load
import json
from random import randint
import pygame
import sys
from models.BugsStatic import BugStatic
from models.Bullet import Bullet
from models.Button import Button
from models.Platform import Platform
from models.Point import Point
from models.Text import Text
from colors import *
from Config import *


def exit():
    print('See you soon!')
    pygame.quit()
    sys.exit()


def randIntPos(axis: str, size):
    if axis == 'x':
        return randint(size, LIMITWIDTHGROUND-size)
    else:
        return randint(150 + size, LIMITHEIGHTGROUND-size)


def createScreen():
    try:
        screen = pygame.display.set_mode(SCREENSIZE)
        screen.fill(WHITE, pygame.Rect(
            0, 0, SCREENWIDTH, SCREENHEIGHT))
        pygame.display.set_caption("PokeBug")
        pygame.display.set_icon(pygame.image.load('assets/totodyle.png'))
        return screen
    except pygame.error as e:
        errMsg(e)


def cleanScreen(screen):
    screenBackroundRect = pygame.Rect(0, 0, SCREENWIDTH, SCREENHEIGHT)
    screen.fill(BLACK, screenBackroundRect)


def drawBackground(screen: pygame.display, background):
    screenBackroundRect = pygame.Rect(0, 0, SCREENWIDTH, SCREENHEIGHT)
    screen.blit(background, screenBackroundRect)


def waitUser():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print('Hasta luego lucassss')
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    print('See ya laater lucass')
                    sys.exit()
                if event.key == pygame.K_SPACE:
                    sys.exit()
                return


def controlesMenu(screen, levelCanvas):

    image = BACKGROUNDCONTROLES
    rectImage = image.get_rect(center=(SCREENWIDTH/2, SCREENHEIGHT/2))
    screen.blit(image, rectImage)

    ButtonCross = Button(40, 40, rectImage.left+70, rectImage.top+70,
                         'X', screen, DARKBLUE, WHITE, 20)
    ButtonCross.CreateButtonMenu()
    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit()
                if event.key == pygame.K_p:
                    return
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if ButtonCross.buttonPressed():
                        return Pause(screen, levelCanvas)


def Pause(screen, levelCanvas):
    muteValue = levelCanvas.getMuteValue()
    if muteValue:
        str = 'Mute On'
    else:
        str = 'Mute Off'

    image = BACKGROUNDPAUSE
    rectImage = image.get_rect(center=(SCREENWIDTH/2, SCREENHEIGHT/2))
    screen.blit(image, rectImage)
    ButtonCross = Button(40, 40, rectImage.left+70, rectImage.top+100,
                         'X', screen, DARKBLUE, WHITE, 20)
    ButtonCross.CreateButtonMenu()

    buttonMute = Button(150, 80, rectImage.centerx - 200, rectImage.centery+80,
                        f'{str}', screen, DARKBLUE, WHITE, 14)
    buttonMute.setFont(14)
    buttonMute.CreateButtonMenu()
    buttonControles = Button(180, 80, rectImage.centerx + 200, rectImage.centery+80,
                             'Controls', screen, DARKBLUE, WHITE, 14)
    buttonControles.setFont(14)
    buttonControles.CreateButtonMenu()

    pygame.display.flip()
    while True:
        if muteValue == False or muteValue == None:
            # ButtonMute.colorText = GREEN
            buttonMute.setText('Mute On', RED)
            # ButtonMute.CreateButtonMenu()
        else:
            # ButtonMute.colorText = RED
            buttonMute.setText('Mute Off', GREEN)
            # ButtonMute.CreateButtonMenu()
            # pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit()
                if event.key == pygame.K_p:
                    return
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if buttonMute.buttonPressed():
                        muteValue = not muteValue
                        buttonMute.setFont(14)
                        buttonMute.CreateButtonMenu()
                        pygame.display.flip()
                    if buttonControles.buttonPressed():
                        controlesMenu(screen, levelCanvas)
                    if ButtonCross.buttonPressed():
                        return


def mainMenu(screen, muteValue: bool):
    background = BACKGROUNSEADAY
    drawBackground(screen, background)
    muteValue = False if muteValue == None else muteValue
    ButtonStart = Button(BUTTONWIDTH, BUTTONHEIGHT,
                         (SCREENWIDTH)/2, (BUTTONHEIGHT*3), 'Start', screen)
    ButtonStart.CreateButtonMenu()
    ButtonOptions = Button(BUTTONWIDTH, BUTTONHEIGHT,
                           (SCREENWIDTH)/2, (SCREENHEIGHT)/2, 'Options', screen)
    ButtonOptions.CreateButtonMenu()
    ButtonExit = Button(BUTTONWIDTH, BUTTONHEIGHT,
                        (SCREENWIDTH)/2, (SCREENHEIGHT-BUTTONHEIGHT*3), 'Exit', screen)
    ButtonExit.CreateButtonMenu()
    pygame.display.flip()
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit()
            if event.type == pygame.MOUSEBUTTONDOWN:

                if event.button == 1:
                    if ButtonStart.buttonPressed():
                        # enviar al usuario al level selector
                        return muteValue
                        # return muteValue
                    if ButtonOptions.buttonPressed():
                        optionMenu(screen, muteValue)
                        return
                    if ButtonExit.buttonPressed():
                        exit()


def optionMenu(screen, muteValue: bool):
    muteValue = False if muteValue == None else muteValue

    drawBackground(screen, BACKGROUNSEADAY)
    ButtonBack = Button(BUTTONWIDTH, BUTTONHEIGHT,
                        (SCREENWIDTH)/2, (BUTTONHEIGHT*3), 'Back', screen)
    ButtonBack.CreateButtonMenu()
    ButtonCredits = Button(BUTTONWIDTH, BUTTONHEIGHT, (SCREENWIDTH)/2,
                           (SCREENHEIGHT-BUTTONHEIGHT*3), 'Credits', screen)
    ButtonCredits.CreateButtonMenu()

    ButtonMute = Button(BUTTONWIDTH, BUTTONHEIGHT,
                        (SCREENWIDTH)/2, (SCREENHEIGHT)/2, 'Mute Off', screen, colorText=GREEN)
    ButtonMute.CreateButtonMenu()
    pygame.display.flip()

    while True:
        if muteValue == False or muteValue == None:
            # ButtonMute.colorText = GREEN
            ButtonMute.setText('Mute On', RED)
            # ButtonMute.CreateButtonMenu()
        else:
            # ButtonMute.colorText = RED

            ButtonMute.setText('Mute Off', GREEN)
            # ButtonMute.CreateButtonMenu()
            # pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if ButtonBack.buttonPressed():
                        mainMenu(screen, muteValue)
                        return
                    if ButtonCredits.buttonPressed():
                        creditsMenu(screen, muteValue)
                        return
                    if ButtonMute.buttonPressed():
                        muteValue = not muteValue
                        ButtonMute.CreateButtonMenu()
                        pygame.display.flip()


def creditsMenu(screen, muteValue: bool):
    background = BACKGROUNSEANIGHT
    drawBackground(screen, background)
    muteValue = muteValue

    ButtonBack = Button(BUTTONWIDTH, BUTTONHEIGHT-20,
                        (BUTTONWIDTH), (SCREENHEIGHT-BUTTONHEIGHT*1.5), 'Back', screen)
    ButtonBack.CreateButtonMenu(BLACK, borderRadius=8)

    ButtonExit = Button(BUTTONWIDTH, BUTTONHEIGHT-20, (SCREENWIDTH -
                        BUTTONWIDTH), (SCREENHEIGHT-BUTTONHEIGHT*1.5), 'Exit', screen)
    ButtonExit.CreateButtonMenu(BLACK, borderRadius=8)

    copywriteImg = loadImage('gameFreak.png')
    copyImgRect = copywriteImg.get_rect()
    copyImgRect = copywriteImg.get_rect(
        center=(copyImgRect.centerx, copyImgRect.centery))
    copyImgRect.center = (((SCREENWIDTH / 2), (0+BUTTONHEIGHT*3)))
    screen.blit(copywriteImg, copyImgRect)

    Text('Juego creado por Mateo Barbato', WHITE, 24, False).blitText(
        screen, (SCREENWIDTH/2, SCREENHEIGHT/2.5), None)
    Text('Idea originada con Pokemon dandole una vuelta creativa', WHITE,
         24, False).blitText(screen, (SCREENWIDTH/2, SCREENHEIGHT/2.25), None)
    Text('Assets obtenidos de la pagina Sprite Database', WHITE, 24,
         False).blitText(screen, (SCREENWIDTH/2, SCREENHEIGHT/2), None)

    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit()
            if event.type == pygame.MOUSEBUTTONDOWN:

                if event.button == 1:
                    if ButtonBack.buttonPressed():
                        optionMenu(screen, muteValue)
                        return
                    if ButtonExit.buttonPressed():
                        sys.exit()


def levelSelector(screen, muteValue):
    drawBackground(screen, BRACKGROUNDGRASS)
    drawBackground(screen, BRACKGROUNDTREES)

    ButtonCross = Button(40, 40, 150, 120,
                         'X', screen, colorbackground=LAVENDER, fontSize=20)

    Level1 = Button(120, 120, SCREENWIDTH/3 - 80,
                    SCREENHEIGHT/2, 'Level 1', screen)
    Level2 = Button(120, 120, SCREENWIDTH/2,
                    SCREENHEIGHT/2, 'Level 2', screen)
    Level3 = Button(120, 120, SCREENWIDTH - SCREENWIDTH/3 + 80,
                    SCREENHEIGHT / 2, 'Level 3', screen)

    Level1.CreateButtonMenu()
    Level2.CreateButtonMenu()
    Level3.CreateButtonMenu()
    ButtonCross.CreateButtonMenu(borderRadius=5)
    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit()
            if event.type == pygame.MOUSEBUTTONDOWN:

                if event.button == 1:
                    if Level1.buttonPressed():
                        return False, 1
                    if Level2.buttonPressed():
                        return False, 2
                    if Level2.buttonPressed():
                        return False, 3
                    if ButtonCross.buttonPressed():
                        return True, 0


# def loadLevel(spriteGroupAll, map):
def levelFinished(screen, background, currentLevel, lastScore, bestScores):
    drawBackground(screen, background)
    if bestScores == 0:
        pass
    else:
        highScores = bestScores
    Text('Your score', WHITE, 42, False).blitText(
        screen, (SCREENWIDTH/2, SCREENHEIGHT/5), WHITE)
    Text(str(lastScore), WHITE, 42, True).blitText(
        screen, (SCREENWIDTH/2, SCREENHEIGHT/4), WHITE)
    print(len(highScores))
    for i, value in enumerate(highScores, 1):

        Text(f'Player {i} : {value["score"]}', WHITE, 22, True).blitText(
            screen, (SCREENWIDTH/2, SCREENHEIGHT/4 + 80*i), WHITE)

    ButtonLevels = Button(180, 40, 150, 120,
                          'Levels', screen, colorbackground=LAVENDER, fontSize=20)
    Restart = Button(160, 70, SCREENWIDTH/2 - 250,
                     SCREENHEIGHT-SCREENHEIGHT/7, 'Restart', screen)
    Continue = Button(160, 70, SCREENWIDTH/2 + 250,
                      SCREENHEIGHT-SCREENHEIGHT/7, 'Continue', screen)
    Restart.setFont(18)
    Restart.CreateButtonMenu()
    Continue.setFont(18)
    Continue.CreateButtonMenu()
    ButtonLevels.CreateButtonMenu(borderRadius=5)
    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit()
            if event.type == pygame.MOUSEBUTTONDOWN:

                if event.button == 1:
                    if Restart.buttonPressed():
                        # enviar al usuario al level selector
                        # print('asd')
                        return True, (currentLevel)
                    if Continue.buttonPressed():
                        if currentLevel == 1:
                            newLevel = 2
                        if currentLevel == 2:
                            newLevel = 3
                        return True, newLevel
                    if ButtonLevels.buttonPressed():
                        return False, 0


def saveScores(data, scoreTotal, levelSelected):
    if levelSelected == 1:
        scoreList = data['Level 1']
    elif levelSelected == 2:
        scoreList = data['Level 2']
    elif levelSelected == 3:
        scoreList = data['Level 3']
    saved = False
    scoreList = sorted(
        scoreList, key=lambda k: k['score'], reverse=True)
    for i in range(len(scoreList)):
        if scoreList[i]['score'] < scoreTotal and saved == False:
            aux = dict()
            aux['score'] = scoreTotal
            scoreList.append(aux)
            saved = True
    scoreList = sorted(
        scoreList, key=lambda k: k['score'], reverse=True)

    if levelSelected == 1:
        data['Level 1'] = scoreList[0:5]
    elif levelSelected == 2:
        data['Level 2'] = scoreList[0:5]
    elif levelSelected == 3:
        data['Level 3'] = scoreList[0:5]

    try:
        with open(r"./db.json", 'w') as dataEnd:
            json.dump(data, dataEnd, indent=2)
    except OSError.filename as Err:
        errMsg(
            "Error while writing the scores to the datafile. The score wont be saved")
        print(Err)
        errMsg(
            'Please validate the files and check again. If the problem persist re-install the files')
    return scoreList[0:5]


def createDefaultDb():
    # arr = []
    data = dict()

    for i in range(1, 4):
        arrLevel = []
        for j in range(1, 6):
            arr = dict()
            arr['score'] = 0
            arrLevel.append(arr)
        data[f'Level {i}'] = arrLevel
    return data


def loadDb():
    try:
        # Intento abrir la base de datos.
        with open('./db.json') as db:
            data = json.load(db)
        # Si abre asigno los datos a las variables del juego ( maxScore y Attempts a superar el max score)
        return data
    except FileNotFoundError as Err:
        # Si falla por no encontrar el archivo me guardo el mensaje del except como Err
        # Despues creo una base de datos nueva (todo en 0) y la utilizo para cargar los datos a mis variables
        # (tambien podes hacer esto al final de juego, yo lo hice del principio para atajarme de errores en medio de la partida)
        data = createDefaultDb()
        with open('./db.json', 'w') as file:
            json.dump(data, file, indent=2)
        # Le muestro los mensajes default y el mensaje de Err que me viene del except
        # la funcion errMsg es una funcion propia que solo aniade espacios arriba y abajo para que sea mas legible todo pero nada mas
        errMsg("Error while trying to read data for the scores")
        print(Err)
        errMsg('Please validate the install and try again. The game can run without it but the db has been reseted to default (0)')
        # por ultimo asigno los datos de la nueva base a las nuevas variables
        return data
