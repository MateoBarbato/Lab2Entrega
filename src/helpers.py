import pygame
import sys


def exit():
    print('Nos vemos en la proxima!')
    pygame.quit()
    sys.exit()

def errMsg(err:str):
    print("")
    print(err)
    print("")

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

def waitUserClick () :
    menuState = 'main'
    while menuState == 'main':
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(event.button)
                if event.button == 1:
                    print('Clickeaste wey')
                return