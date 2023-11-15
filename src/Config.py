import pygame


SCREENHEIGHT = 800
SCREENWIDTH = 1100
SCREENSIZE = (SCREENWIDTH, SCREENHEIGHT)
BUTTONWIDTH = 250
BUTTONHEIGHT = 70
MUTESTATE = False
GRAVITY = 2.5
PLAYERVELOCITY = 3
SPIRTESIZE = 32


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
