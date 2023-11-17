from ast import main
from random import randint
import secrets
from turtle import color
import pygame
import sys
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
        return randint(0, SCREENWIDTH-axisSize)
    else:
        return randint(0, SCREENHEIGHT-axisSize)


def createScreen():
    try:
        screen = pygame.display.set_mode(SCREENSIZE)
        screen.fill(WHITE, pygame.Rect(0, 0, SCREENWIDTH, SCREENHEIGHT))
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
    # muteValue = muteValue if muteValue != None else False
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
    # muteValue = muteValue if muteValue != None else False
    background = BACKGROUNSEADAY
    drawBackground(screen, background)
    ButtonBack = Button(BUTTONWIDTH, BUTTONHEIGHT,
                        (SCREENWIDTH)/2, (BUTTONHEIGHT*3), 'Back', screen)
    ButtonBack.CreateButtonMenu()
    ButtonCredits = Button(BUTTONWIDTH, BUTTONHEIGHT, (SCREENWIDTH)/2,
                           (SCREENHEIGHT-BUTTONHEIGHT*3), 'Credits', screen)
    ButtonCredits.CreateButtonMenu()

    ButtonMute = Button(BUTTONWIDTH, BUTTONHEIGHT,
                        (SCREENWIDTH)/2, (SCREENHEIGHT)/2, 'Mute On', screen)

    while True:
        if muteValue == False or muteValue == None:
            ButtonMute.colorText = GREEN
            ButtonMute.CreateButtonMenu()
        else:
            ButtonMute.colorText = RED
            ButtonMute.CreateButtonMenu()
        pygame.display.update(ButtonMute.rect)
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
    backgroundgrass = BRACKGROUNDGRASS
    backgroundtrees = BRACKGROUNDTREES
    drawBackground(screen, backgroundgrass)
    drawBackground(screen, backgroundtrees)

    ButtonExit = Button(40, 40, 150, (0+BUTTONHEIGHT*2),
                        'X', screen, colorbackground=LAVENDER)

    Button(50, 50, ButtonExit.rect.centerx, (ButtonExit.rect.centery), '',
           screen, colorbackground=LAVENDERDARK).CreateButtonMenu(screen, borderRadius=5)

    ButtonExit.setFont(20, bold=True)
    ButtonExit.CreateButtonMenu(screen, borderRadius=5)

    Level1 = Button(120, 120, SCREENWIDTH/2,
                    SCREENHEIGHT/3, 'Level 1', screen,)
    Level1.CreateButtonMenu(screen)

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
                        return muteValue
                    # if ButtonOptions.buttonPressed():
                    #     return
                    if ButtonExit.buttonPressed():
                        mainMenu(screen, False)
