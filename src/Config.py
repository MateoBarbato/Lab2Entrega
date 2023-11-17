import pygame


SCREENHEIGHT = 800
SCREENWIDTH = 1100
SCREENSIZE = (SCREENWIDTH, SCREENHEIGHT)
BUTTONWIDTH = 250
BUTTONHEIGHT = 70
MUTESTATE = False
GRAVITY = 3
PLAYERVELOCITY = 3
SPIRTESIZEMAINWIDTH = 24
SPIRTESIZEMAINHEIGHT = 28
SPIRTEMAINROW = 5
SPIRTEMAINCOL = 4
SPRITEBUGSIZE = 32
SPRITEBUGROW = 3
SPRITEBUGCOL = 4
ANIMATIONSPEED = 250


def loadImage(image: str):
    try:
        imgToLoad = pygame.image.load(f'assets/{image}')
        return imgToLoad
    except FileNotFoundError as e:
        errMsg(e)
        print(f'{image} fail to load')
        errMsg('Error loading an image, exiting...')
        exit()


def loadBackground(image: str = 'fondoMarDia.png'):
    try:
        background = pygame.image.load(f'assets/{image}')
        background = pygame.transform.scale(
            background, (SCREENWIDTH, SCREENHEIGHT))
        return background
    except FileNotFoundError as e:
        errMsg(e)
        errMsg('Error loading the backgorund, exiting...')
        exit()


def errMsg(err: str):
    print("")
    print(err)
    print("")


BACKGROUNSEADAY = loadBackground()
BACKGROUNSEANIGHT = loadBackground('fondoMarNoche.png')
BRACKGROUNDGRASS = loadBackground('grass.png')
BRACKGROUNDTREES = loadBackground('trees.png')
