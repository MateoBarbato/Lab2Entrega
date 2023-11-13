from random import randint
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

def errMsg(err:str):
    print("")
    print(err)
    print("")

def randIntPos(axis):
    if axis=='x':
       return randint(0,SCREENWIDTH)
    else:
        return randint(0,SCREENHEIGHT)

def cleanScreen(screen):
    screenBackroundRect = pygame.Rect(0,0,SCREENWIDTH,SCREENHEIGHT)
    screen.fill(BLACK,screenBackroundRect)

def loadBackground(image:str='fondoMarDia.png'):
    try:
        background = pygame.image.load(rf'assets/{image}')
        background = pygame.transform.scale(background,(SCREENWIDTH,SCREENHEIGHT))
        return background
    except FileNotFoundError as e:
        errMsg(e)
        errMsg('Error loading the backgorund, black backround instead')
        exit()

def drawBackground(screen:pygame.display,background):
    screenBackroundRect = pygame.Rect(0,0,SCREENWIDTH,SCREENHEIGHT)
    screen.blit(background,screenBackroundRect)

def waitUser ():
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

def mainMenu (screen,muteValue:bool):
    background = loadBackground()
    drawBackground(screen,background)
    muteValue = muteValue if muteValue !=None else False
    menuState = 'main'
    ButtonStart = Button(BLACK,BUTTONWIDTH,BUTTONHEIGHT,(SCREENWIDTH)/2,(BUTTONHEIGHT*3),'Start',screen)
    ButtonStart.CreateButtonMenu(screen)
    ButtonOptions = Button(BLACK,BUTTONWIDTH,BUTTONHEIGHT,(SCREENWIDTH)/2,(SCREENHEIGHT)/2,'Options',screen)
    ButtonOptions.CreateButtonMenu(screen)
    ButtonExit = Button(BLACK,BUTTONWIDTH,BUTTONHEIGHT,(SCREENWIDTH)/2,(SCREENHEIGHT-BUTTONHEIGHT*3),'Exit',screen)
    ButtonExit.CreateButtonMenu(screen)
    pygame.display.flip()
    while menuState == 'main':
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if event.button == 1:
                    if ButtonStart.buttonPressed():
                        return muteValue
                    if ButtonOptions.buttonPressed():
                        optionMenu(screen,muteValue)
                        return
                    if ButtonExit.buttonPressed():
                        exit()

def optionMenu(screen,muteValue:bool):
        muteValue = muteValue if muteValue !=None else False
        background = loadBackground()
        drawBackground(screen,background)
        ButtonBack = Button(BLACK,BUTTONWIDTH,BUTTONHEIGHT,(SCREENWIDTH)/2,(BUTTONHEIGHT*3),'Back',screen)
        ButtonBack.CreateButtonMenu(screen)
        ButtonCredits = Button(BLACK,BUTTONWIDTH,BUTTONHEIGHT,(SCREENWIDTH)/2,(SCREENHEIGHT-BUTTONHEIGHT*3),'Credits',screen)
        ButtonCredits.CreateButtonMenu(screen)
        while True:
            if muteValue == False or muteValue == None:
                ButtonMute = Button(BLACK,BUTTONWIDTH,BUTTONHEIGHT,(SCREENWIDTH)/2,(SCREENHEIGHT)/2,'Mute Off',screen)
                ButtonMute.CreateButtonMenu(screen,BLACK,LAVENDER)
            else:
                ButtonMute = Button(BLACK,BUTTONWIDTH,BUTTONHEIGHT,(SCREENWIDTH)/2,(SCREENHEIGHT)/2,'Mute On',screen)
                ButtonMute.CreateButtonMenu(screen,RED,LAVENDER)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if ButtonBack.buttonPressed():
                            mainMenu(screen,muteValue)
                            return
                        if ButtonMute.buttonPressed():
                            muteValue = not muteValue
                        if ButtonCredits.buttonPressed():
                            creditsMenu(screen,muteValue)
                            return
                        
def creditsMenu(screen,muteValue:bool):
        background = loadBackground('fondoMarNoche.png')
        drawBackground(screen,background)
        muteValue = muteValue if muteValue !=None else False
        ButtonBack = Button(BLACK,BUTTONWIDTH,BUTTONHEIGHT-20,(BUTTONWIDTH),(SCREENHEIGHT-BUTTONHEIGHT*1.5),'Back',screen)
        ButtonBack.CreateButtonMenu(screen,BLACK,LAVENDER,borderRadius=8)

        ButtonExit = Button(BLACK,BUTTONWIDTH,BUTTONHEIGHT-20,(SCREENWIDTH-BUTTONWIDTH),(SCREENHEIGHT-BUTTONHEIGHT*1.5),'Exit',screen)
        ButtonExit.CreateButtonMenu(screen,BLACK,LAVENDER,borderRadius=8)

        Text('Juego creado por Mateo Barbato',WHITE,24,False).blitText(screen,(SCREENWIDTH/2,SCREENHEIGHT/2.5),None)
        Text('Idea originada con Pokemon dandole una vuelta creativa',WHITE,24,False).blitText(screen,(SCREENWIDTH/2,SCREENHEIGHT/2.25),None)
        Text('Assets obtenidos de la pagina Sprite Database',WHITE,24,False).blitText(screen,(SCREENWIDTH/2,SCREENHEIGHT/2),None)

        pygame.display.flip()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if event.button == 1:
                        if ButtonBack.buttonPressed():
                            optionMenu(screen,muteValue)
                            return
                        if ButtonExit.buttonPressed():
                            sys.exit()