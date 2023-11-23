from ast import main
from random import randint
import pygame
import sys
from models.BugsStatic import BugStatic
from models.Bullet import Bullet
from models.Button import Button
from models.Text import Text
from colors import *
from Config import *


def exit():
    print('See you soon!')
    pygame.quit()
    sys.exit()


def randIntPos(axis, axisSize):
    if axis == 'x':
        return randint(axisSize, LIMITWIDTHGROUND-axisSize)
    else:
        return randint(axisSize, LIMITHEIGHTGROUND-axisSize)


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


def mainMenu(screen, muteValue: bool):
    background = BACKGROUNSEADAY
    drawBackground(screen, background)

    muteValue = muteValue
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
                        return levelSelector(screen, muteValue)
                        # return muteValue
                    if ButtonOptions.buttonPressed():
                        optionMenu(screen, muteValue)
                        return
                    if ButtonExit.buttonPressed():
                        exit()


def optionMenu(screen, muteValue: bool):
    print(muteValue)
    muteValue = muteValue

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
    Level1 = Button(120, 120, SCREENWIDTH/2,
                    SCREENHEIGHT/3, 'Level 1', screen)

    Level1.CreateButtonMenu()
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
                        # enviar al usuario al level selector
                        # print('asd')
                        return muteValue
                    # if ButtonOptions.buttonPressed():
                    #     return
                    if ButtonCross.buttonPressed():
                        mainMenu(screen, False)
