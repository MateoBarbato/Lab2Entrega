import pygame
import sys
from models.Button import Button
from colors import *
from Config import *

def exit():
    print('Nos vemos en la proxima!')
    pygame.quit()
    sys.exit()

def errMsg(err:str):
    print("")
    print(err)
    print("")

def cleanScreen(screen):
    screenBackroundRect = pygame.Rect(0,0,SCREENWIDTH,SCREENHEIGHT)
    screen.fill(BLACK,screenBackroundRect)
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
                return

def waitUserClick (screen,muteState):
    menuState = 'main'
    muteState = muteState

    ButtonStart = Button(BLACK,120,120,(SCREENWIDTH-120)/2,(SCREENHEIGHT-120*5),'Start',screen)
    ButtonStart.CreateButtonMenu(screen)
    ButtonOptions = Button(BLACK,120,120,(SCREENWIDTH-120)/2,(SCREENHEIGHT-120)/2,'Options',screen)
    ButtonOptions.CreateButtonMenu(screen)
    ButtonExit = Button(BLACK,120,120,(SCREENWIDTH-120)/2,(SCREENHEIGHT-120*2.5),'Exit',screen)
    ButtonExit.CreateButtonMenu(screen)

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
                    if ButtonStart.rect.collidepoint(pos[0],pos[1]):
                        print('a juegar')
                        return muteState
                    if ButtonOptions.rect.collidepoint(pos[0],pos[1]):
                        menuState = 'options'
                        break
                    if ButtonExit.rect.collidepoint(pos[0],pos[1]):
                        exit()

    ButtonBack = Button(BLACK,120,120,(SCREENWIDTH-120)/2,(SCREENHEIGHT-120*5),'Back',screen)
    ButtonBack.CreateButtonMenu(screen)
    ButtonCredits = Button(BLACK,120,120,(SCREENWIDTH-120)/2,(SCREENHEIGHT-120*2.5),'Credits',screen)
    ButtonCredits.CreateButtonMenu(screen)
    while menuState == 'options':
        if muteState == False:
            # cleanScreen(screen)
            ButtonMute = Button(BLACK,120,120,(SCREENWIDTH-120)/2,(SCREENHEIGHT-120)/2,'Mute Off',screen)
            ButtonMute.CreateButtonMenu(screen,GREEN,LAVENDER)
        else:
            # cleanScreen(screen)
            ButtonMute = Button(BLACK,120,120,(SCREENWIDTH-120)/2,(SCREENHEIGHT-120)/2,'Muted On',screen)
            ButtonMute.CreateButtonMenu(screen,RED,LAVENDER)
        pygame.display.flip()
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
                        menuState = 'main'
                        break
                    if ButtonMute.rect.collidepoint(pos[0],pos[1]):
                        muteState = not muteState
                        # OBTENGO EL TAMAÑO DEL BOTON A BORRAR Y LO PINTO, AL SALIR DEL LOOP SE VUEVLEN A PINTAR VALIDANDO EL ESTADO DEL MUTE
                        ButtonMuteSurface = pygame.Surface(ButtonMute.rect.size)
                        ButtonMuteSurface.fill(BLACK)
                        break
                    if ButtonCredits.rect.collidepoint(pos[0],pos[1]):
                        # drawCredits()
                        print('asd')
        pygame.display.flip()
    cleanScreen(screen)