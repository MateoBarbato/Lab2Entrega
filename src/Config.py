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
PLAYERVELOCITY = 4.5
ENEMYVELOCITY = 2
PLAYERHEIGHT = 64
PLAYERWIDTH = 46
SPIRTESIZEMAINWIDTH = 24
SPIRTESIZEMAINHEIGHT = 28
SPIRTEMAINROW = 5
SPIRTEMAINCOL = 4
SPRITEBUGSIZE = 32
SPRITEBUGROW = 3
SPRITEBUGCOL = 4
ANIMATIONSPEED = 250
BULLETSIZE = 30
BUGSIZE = 60
BUGSIZEMOVING = 62
BLOCKWIDTH = 60
BLOCKHEIGTH = 80
# JUMPMAXHEIGH = -120
JUMPMAXHEIGH = -220


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
SPRITEBELLSPROUT = loadImage('pokemon4.png')
SPRITECANGREJO = loadImage('pokemon5.png')
PLAYERSHEET = loadImage('LucasSprite.png')
PLAYERSHEETATTACK = loadImage('LucasSpritewithAttack.png')
BULLETPLANT = loadImage('plantBullet.png')
BULLETWATER = loadImage('waterBullet.png')
FRUIT1SHEET = loadImage('point1.png')
FRUIT2SHEET = loadImage('point2.png')
FRUIT3SHEET = loadImage('point3.png')

level_map1 = [
    '1111111111111111111',
    '1111111111111111111',
    '1111111111111111111',
    '1000000000000011111',
    '100P000000000000001',
    '10010P0000000000001',
    '1000010P00000P0P001',
    '1000000100P00000001',
    '1000000000111111111',
    '1000P0P000000000001',
    '1000000000000000001',
    '1111111111111000001',
    '1111111111111111111',
]
