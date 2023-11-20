import pygame


SCREENHEIGHT = 800
SCREENWIDTH = 1200
SCREENSIZE = (SCREENWIDTH, SCREENHEIGHT)
LIMITHEIGHTGROUND = 760
LIMITWIDTHGROUND = 1140
BUTTONWIDTH = 250
BUTTONHEIGHT = 70
MUTESTATE = False
GRAVITY = 3
PLAYERVELOCITY = 3
ENEMYVELOCITY = 2
PLAYERHEIGHT = 80
PLAYERWIDTH = 60
SPIRTESIZEMAINWIDTH = 24
SPIRTESIZEMAINHEIGHT = 28
SPIRTEMAINROW = 5
SPIRTEMAINCOL = 4
SPRITEBUGSIZE = 32
SPRITEBUGROW = 3
SPRITEBUGCOL = 4
ANIMATIONSPEED = 250
BULLETSIZE = 30
BUGSIZE = 80
BLOCKWIDTH = 60
BLOCKHEIGTH = 80
JUMPMAXHEIGH = -120
# JUMPMAXHEIGH = -84


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
BACKGROUNDMAIN = loadBackground('BossLevelV1.png')
BACKGROUNDSECRETLEVEL = loadBackground('fondo.png')
BACKGROUNDLEVEL1 = loadBackground('Level1V1.png')
