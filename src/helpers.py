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
    """Exits the game and prints a farewell message."""
    print('See you soon!')
    pygame.quit()
    sys.exit()


def randIntPos(axis: str, size):
    """Generates a random integer position within the specified axis and size limits."""
    if axis == 'x':
        return randint(size, LIMITWIDTHGROUND-size)
    else:
        return randint(150 + size, LIMITHEIGHTGROUND-size)


def createScreen():
    """Initializes the game screen and sets its caption."""
    try:
        screen = pygame.display.set_mode(SCREENSIZE)
        screen.fill(WHITE, pygame.Rect(
            0, 0, SCREENWIDTH, SCREENHEIGHT))
        pygame.display.set_caption("PokeBug")
        pygame.display.set_icon(pygame.image.load(
            os.path.join('assets', 'images', 'totodyle.png')))
        return screen
    except pygame.error as e:
        errMsg(e)


def cleanScreen(screen):
    """Clears the game screen by filling it with black color."""
    screenBackroundRect = pygame.Rect(0, 0, SCREENWIDTH, SCREENHEIGHT)
    screen.fill(BLACK, screenBackroundRect)


def drawBackground(screen: pygame.display, background):
    """Draws the specified background image on the game screen."""
    screenBackroundRect = pygame.Rect(0, 0, SCREENWIDTH, SCREENHEIGHT)
    screen.blit(background, screenBackroundRect)


def controlesMenu(screen, levelCanvas):
    """Displays the controls menu and handles user interaction."""
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
    """Displays the pause menu and handles user interaction."""
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


def mainMenu(screen, mainMusic, muteValue: bool):

    if muteValue:
        mainMusic.set_volume(0)
    else:
        mainMusic.set_volume(0.5)
    """Displays the main menu and handles user interaction,game settings and credits screen."""
    background = BACKGROUNSEADAY
    drawBackground(screen, background)
    muteValue = False if muteValue == None else True
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
                        optionMenu(screen, mainMusic, muteValue)
                        return
                    if ButtonExit.buttonPressed():
                        exit()


def optionMenu(screen, mainMusic, muteValue: bool):
    """Displays the options menu and handles user interaction."""
    muteValue = True if muteValue == None else False
    drawBackground(screen, BACKGROUNSEADAY)
    ButtonBack = Button(BUTTONWIDTH, BUTTONHEIGHT,
                        (SCREENWIDTH)/2, (BUTTONHEIGHT*3), 'Back', screen)
    ButtonBack.CreateButtonMenu()
    ButtonCredits = Button(BUTTONWIDTH, BUTTONHEIGHT, (SCREENWIDTH)/2,
                           (SCREENHEIGHT-BUTTONHEIGHT*3), 'Credits', screen)
    ButtonCredits.CreateButtonMenu()

    ButtonMute = Button(BUTTONWIDTH, BUTTONHEIGHT,
                        (SCREENWIDTH)/2, (SCREENHEIGHT)/2, f'Mute', screen, colorText=GREEN)
    ButtonMute.CreateButtonMenu()
    pygame.display.flip()

    while True:
        if muteValue == False or muteValue == None:
            # ButtonMute.colorText = GREEN
            ButtonMute.setText('Mute', RED)
            # ButtonMute.CreateButtonMenu()
        else:
            # ButtonMute.colorText = RED

            ButtonMute.setText('Mute', GREEN)
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
                        mainMenu(screen, mainMusic, muteValue)
                        return
                    if ButtonCredits.buttonPressed():
                        creditsMenu(screen, mainMusic, muteValue)
                        return
                    if ButtonMute.buttonPressed():
                        muteValue = not muteValue
                        ButtonMute.CreateButtonMenu()
                        pygame.display.flip()


def creditsMenu(screen, mainMusic, muteValue: bool):
    """Displays the credits menu and handles user interaction."""
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
                        optionMenu(screen, mainMusic, muteValue)
                        return
                    if ButtonExit.buttonPressed():
                        sys.exit()


def levelSelector(screen, dataStars):
    """Loads the specified level into the game.

    Parameters:
        spriteGroupAll (pygame.sprite.Group): The group of all sprites in the game.
        map (list of lists): The level map.

    Additional Explanation:
        This function reads the level map and creates the corresponding sprites for the level.
        It also sets the starting positions of the player and other objects in the level.
    """

    drawBackground(screen, BRACKGROUNDGRASS)
    drawBackground(screen, BRACKGROUNDTREES)
    ButtonHeight = 90
    ButtonWidth = 130
    ButtonCross = Button(40, 40, 150, 120,
                         'X', screen, colorbackground=LAVENDER, fontSize=20)
    # -------------------------------------------------------------------------
    Level1 = Button(ButtonWidth, ButtonHeight, SCREENWIDTH/3 - 80,
                    SCREENHEIGHT/2.5, 'Level 1', screen, GREENMENU, WHITE)
    Text(f'{dataStars["1"]}/3 Stars', YELLOW, 24, False).blitText(
        screen, (SCREENWIDTH/3 - 80, (SCREENHEIGHT/2.5)+70), None)
    # -------------------------------------------------------------------------
    Level2 = Button(ButtonWidth, ButtonHeight, SCREENWIDTH/2,
                    SCREENHEIGHT/2.5, 'Level 2', screen, GREENMENU, WHITE)
    Text(f'{dataStars["2"]}/3 Stars', YELLOW, 24, False).blitText(
        screen, (SCREENWIDTH/2, (SCREENHEIGHT/2.5)+70), None)
    # -------------------------------------------------------------------------
    Level3 = Button(ButtonWidth, ButtonHeight, SCREENWIDTH - SCREENWIDTH/3 + 80,
                    SCREENHEIGHT / 2.5, 'Level 3', screen, GREENMENU, WHITE)
    Text(f'{dataStars["3"]}/3 Stars', YELLOW, 24, False).blitText(
        screen, (SCREENWIDTH - SCREENWIDTH/3 + 80, (SCREENHEIGHT/2.5)+70), None)
    # -------------------------------------------------------------------------
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
                        if dataStars['1'] > 1:
                            return False, 2
                        else:
                            pass
                    if Level3.buttonPressed():
                        if dataStars['2'] > 1:
                            return False, 3
                        else:
                            pass
                    if ButtonCross.buttonPressed():
                        return True, 0


# def loadLevel(spriteGroupAll, map):
def levelFinished(screen, background, currentLevel, lastScore, bestScores):
    """Displays the level finished screen and handles user interaction.

    Parameters:
        screen (pygame.Surface): The pygame Surface object representing the game screen.
        background (pygame.Surface): The background image to draw.
        currentLevel (int): The current level number.
        lastScore (int): The score for the current level.
        bestScores (list of dicts): The list of best scores for each level.

    Return Value:
        A tuple of two booleans:
            * The first boolean indicates whether to restart the current level.
            * The second boolean indicates whether to go to the level selector.

    Additional Explanation:
        This function displays the level finished screen, showing the player's score and the best scores.
        It handles user interaction by checking for mouse clicks on the buttons.
    """
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
                        return True, (currentLevel)
                    if Continue.buttonPressed():
                        if currentLevel == 1:
                            newLevel = 2
                            if lastScore > 60:
                                return True, newLevel
                            else:
                                pass
                        if currentLevel == 2:
                            newLevel = 3
                            if lastScore > 60:
                                return True, newLevel
                            else:
                                pass
                        if currentLevel == 3:
                            return False, 0

                    if ButtonLevels.buttonPressed():
                        return False, 0


def saveScores(data, scoreTotal, levelSelected):
    """
    This function saves the scores of the game in a JSON file.

    Args:
        data (dict): The JSON data that contains the scores of the game.
        scoreTotal (int): The score of the current game.
        levelSelected (int): The level of the game that was played.

    Returns:
        list: The list of the top 5 scores for the selected level.
    """
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


def saveScoresLevel(dataStars, lastScore, levelSelected):
    # dict['1'] : 0, 112, '1'
    levelSelected = str(levelSelected)
    dictionarioLevel = dataStars
    if lastScore > 60 and lastScore < 120:
        dictionarioLevel[levelSelected] = 1
    elif lastScore > 120 and lastScore < 180:
        dictionarioLevel[levelSelected] = 2
    elif lastScore > 180:
        dictionarioLevel[levelSelected] = 3
    else:
        dictionarioLevel[levelSelected] = 0

    try:
        with open(r"./dbLevel.json", 'w') as dataEnd:
            json.dump(dictionarioLevel, dataEnd, indent=2)
    except OSError.filename as Err:
        errMsg(
            "Error while writing the scores to the datafile. The score wont be saved")
        print(Err)
        errMsg(
            'Please validate the files and check again. If the problem persist re-install the files')

    pass


def createDefaultDb():
    """
    This function creates a default JSON file with empty data for the scores of the game.

    Returns:
        dict: The JSON data with the empty scores.
    """
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


def createDefaultLevelDb():
    """
    This function creates a default JSON file with empty data for the scores of the Levels.

    Returns:
        dict: The JSON data with the empty scores.
    """
    data = dict()

    for i in range(1, 4):
        data[f'{i}'] = 0
    return data


def loadLevelDb():
    try:
        # Intento abrir la base de datos.
        with open('./dbLevel.json') as db:
            data = json.load(db)
        # Si abre asigno los datos a las variables del juego ( maxScore y Attempts a superar el max score)
        return data
    except FileNotFoundError as Err:
        # Si falla por no encontrar el archivo me guardo el mensaje del except como Err
        # Despues creo una base de datos nueva (todo en 0) y la utilizo para cargar los datos a mis variables
        # (tambien podes hacer esto al final de juego, yo lo hice del principio para atajarme de errores en medio de la partida)
        data = createDefaultLevelDb()
        with open('./dbLevel.json', 'w') as file:
            json.dump(data, file, indent=2)
        # Le muestro los mensajes default y el mensaje de Err que me viene del except
        # la funcion errMsg es una funcion propia que solo aniade espacios arriba y abajo para que sea mas legible todo pero nada mas
        errMsg("Error while trying to read data for the scores")
        print(Err)
        errMsg('Please validate the install and try again. The game can run without it but the db has been reseted to default (0)')
        # por ultimo asigno los datos de la nueva base a las nuevas variables
        return data
