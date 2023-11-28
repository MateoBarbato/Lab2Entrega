import os
import pygame
pygame.mixer.init()

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
BLOCKWIDTH = 64
# JUMPMAXHEIGH = -120
JUMPMAXHEIGH = -220


def loadImage(image: str):
    try:
        imgToLoad = pygame.image.load(os.path.join('assets', 'images', image))
        return imgToLoad
    except FileNotFoundError as e:
        errMsg(e)
        print(f'{image} fail to load')
        errMsg('Error loading an image, exiting...')
        exit()


def loadBackground(image: str = 'fondoMarDia.png', scale=(SCREENWIDTH, SCREENHEIGHT)):
    try:
        background = pygame.image.load(os.path.join('assets', 'images', image))
        background = pygame.transform.scale(
            background, scale)
        return background
    except FileNotFoundError as e:
        errMsg(e)
        errMsg('Error loading the backgorund, exiting...')
        exit()


def loadSound(sound: str):
    try:
        soundLoaded = pygame.mixer.Sound(
            os.path.join('assets', 'audio', sound))
        return soundLoaded
    except FileNotFoundError as e:
        errMsg(e)
        errMsg('Error loading the backgorund, exiting...')
        exit()


def errMsg(err: str):
    print("")
    print(err)
    print("")


ICONGAME = loadImage('totodyle.png')
BACKGROUNSEADAY = loadBackground()
BACKGROUNSEANIGHT = loadBackground('fondoMarNoche.png')
BRACKGROUNDGRASS = loadBackground('grass.png')
BRACKGROUNDTREES = loadBackground('trees.png')
BACKGROUNDPAUSE = loadBackground('Pause.png', (800, 450))
BACKGROUNDCONTROLES = loadBackground('controles.png', (800, 450))
BACKGROUNDSECRETLEVEL = loadBackground('fondo.png')
BACKGROUNDLEVEL1 = loadBackground('Level1V1.png')
BACKGROUNDLEVEL2 = loadBackground('Level2V1.png')
BACKGROUNDLEVEL3 = loadBackground('BossLevelV1.png')
SPRITEBELLSPROUT = loadImage('pokemon4.png')
SPRITECANGREJO = loadImage('pokemon5.png')
TRAPTEST = loadImage('trap.png')
PLAYERSHEET = loadImage('LucasSprite.png')
PLAYERSHEETATTACK = loadImage('LucasSpritewithAttack.png')
BULLETPLANT = loadImage('plantBullet.png')
BULLETWATER = loadImage('waterBullet.png')
BULLETPLAYER = loadImage('playerbullet.png')
BULLETBOSS = loadImage('bossbullet.png')
FRUIT1SHEET = loadImage('point1.png')
FRUIT2SHEET = loadImage('point2.png')
FRUIT3SHEET = loadImage('point3.png')
VIDAPOINT = loadImage('vidaPoint.png')
CORAZON = loadImage('vida.png')
BOOSSHEET = loadImage('lugia.png')
DAMAGEPLAYER = loadSound('damage.wav')
DYINGPLAYER = loadSound('dyingPlayer.wav')
LIVEUP = loadSound('liveUp2sec.wav')
SHOOT = loadSound('plantShoot.wav')
TRAPSPIKES = loadSound('trapSpikes.wav')
ADDPOINT = loadSound('point.wav')
DAMAGEENEMY = loadSound('damageEnemy.wav')
MUSICMENU = loadSound('musicaMenus.mp3')
GAMEMUSIC = loadSound('musicLevel.mp3')
