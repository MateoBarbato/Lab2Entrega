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

def cleanScreen(screen):
    screenBackroundRect = pygame.Rect(0,0,SCREENWIDTH,SCREENHEIGHT)
    screen.fill(BLACK,screenBackroundRect)

def drawBackground(screen:pygame.display,image:str='fondo.png'):
    screenBackroundRect = pygame.Rect(0,0,SCREENWIDTH,SCREENHEIGHT)
    try:
        fondo = pygame.image.load(rf'assets/{image}')
        fondo = pygame.transform.scale(fondo,(SCREENWIDTH,SCREENHEIGHT))
        
    except FileNotFoundError as e:
        errMsg(e)
        errMsg('Error loading the backgorund, black backround instead')
        screen.fill(BLACK,screenBackroundRect)
    screen.blit(fondo,screenBackroundRect)
    pygame.display.flip()

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
    drawBackground(screen)
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
                        break
                    if ButtonExit.buttonPressed():
                        exit()

def optionMenu(screen,muteValue:bool):
        muteValue = muteValue 
        drawBackground(screen)
        ButtonBack = Button(BLACK,BUTTONWIDTH,BUTTONHEIGHT,(SCREENWIDTH)/2,(BUTTONHEIGHT*3),'Back',screen)
        ButtonBack.CreateButtonMenu(screen)
        ButtonCredits = Button(BLACK,BUTTONWIDTH,BUTTONHEIGHT,(SCREENWIDTH)/2,(SCREENHEIGHT-BUTTONHEIGHT*3),'Credits',screen)
        ButtonCredits.CreateButtonMenu(screen)
        pygame.display.flip()
        while True:
            if muteValue == False or muteValue == None:
                ButtonMute = Button(BLACK,BUTTONWIDTH,BUTTONHEIGHT,(SCREENWIDTH)/2,(SCREENHEIGHT)/2,'Mute Off',screen)
                ButtonMute.CreateButtonMenu(screen,BLACK,LAVENDER)
                pygame.display.flip()
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
                            print('asd')

def creditsMenu(screen,muteValue:bool):
        drawBackground(screen,'fondoMarDia.png')

        ButtonBack = Button(BLACK,BUTTONWIDTH,BUTTONHEIGHT-20,(BUTTONWIDTH),(SCREENHEIGHT-BUTTONHEIGHT*1.5),'Back',screen)
        ButtonBack.CreateButtonMenu(screen,BLACK,PURPLE,borderRadius=8)

        ButtonExit = Button(BLACK,BUTTONWIDTH,BUTTONHEIGHT-20,(SCREENWIDTH-BUTTONWIDTH),(SCREENHEIGHT-BUTTONHEIGHT*1.5),'Exit',screen)
        ButtonExit.CreateButtonMenu(screen,BLACK,PURPLE,borderRadius=8)

        Text('Juego creado por Mateo Barbato',WHITE,24).blitText(screen,(SCREENWIDTH/2,SCREENHEIGHT/2.5),BLACK,None)
        Text('Idea originada con Pokemon dandole una vuelta creativa',WHITE,24).blitText(screen,(SCREENWIDTH/2,SCREENHEIGHT/2.25),BLACK,None)
        Text('Assets obtenidos de la pagina Sprite Database',WHITE,24).blitText(screen,(SCREENWIDTH/2,SCREENHEIGHT/2),BLACK,None)

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