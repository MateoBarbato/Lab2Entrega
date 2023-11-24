from random import randint
from re import S
import pygame
from Config import BULLETSIZE, ENEMYVELOCITY, GRAVITY, LIMITHEIGHTGROUND, LIMITWIDTHGROUND, SCREENHEIGHT, SCREENWIDTH, SPRITEBUGCOL, SPRITEBUGROW, BLOCKWIDTH, SPRITEBUGSIZE, ANIMATIONSPEED, SPRITECANGREJO, loadImage
from models.Bullet import Bullet

from spriteSheet import loadSprites


class Bug(pygame.sprite.Sprite):

    def __init__(self, groups, bulletsGroup, x: int, y: int, width: int, height: int, screen: pygame.display, typeElement: str, imageSheet: str = None) -> None:
        super().__init__(groups)
        self.groupsVar = groups
        self.x = x
        self.y = y
        self.speed = 1
        self.pos = (x, y)
        self.width = width
        self.height = height
        self.currentFrame = 0
        self.sheet = imageSheet
        self.spriteKeys = ['down', 'rigth', 'left']
        self.animations = loadSprites(
            self.sheet, SPRITEBUGSIZE, SPRITEBUGSIZE, SPRITEBUGROW, SPRITEBUGCOL, self.spriteKeys)
        self.image = self.setImage(self.animations['down'][self.currentFrame])
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
        self.mask = pygame.mask.from_surface(self.image)
        self.screen = screen
        self.lastUpdate = pygame.time.get_ticks()
        self.animationSpeed = ANIMATIONSPEED
        self.ammountOfFrames = SPRITEBUGCOL
        self.currentFacing = 'left'
        self.bullets = bulletsGroup
        self.falling = True
        self.typeElement = typeElement
        self.velocityX = ENEMYVELOCITY
        self.randDir()
        # self.setRandomPos()

    def setRandomPos(self):
        x = randint(0, LIMITWIDTHGROUND-self.width)
        y = self.y
        self.x = x
        self.y = y
        return (x, y)

    def delBug(self):
        del self

    def randDir(self):
        if randint(0, 1) == 0:
            self.currentFacing = 'left'
            self.velocityX = -2
        else:
            self.currentFacing = 'rigth'
            self.velocityX = 2

    def moverAuto(self):
        # if self.rect.bottom > LIMITHEIGHTGROUND:
        #     self.falling = False
        if self.falling:
            self.rect.y += GRAVITY

        if self.falling == False:
            # if self.rect.left < BLOCKWIDTH:
            #     print('pared izq')
            #     # ahora verifica ancho de nivel, falta verificar colisiones con futuros bloques
            #     self.currentFacing = 'rigth'
            # elif self.rect.right > LIMITWIDTHGROUND:
            #     print('pared derecha')
            #     # ahora verifica ancho de nivel, falta verificar colisiones con futuros bloques
            #     self.currentFacing = 'left'

            if self.currentFacing == 'left':
                self.animateDirection()
                self.rect.x += self.velocityX
            elif self.currentFacing == 'rigth':
                self.animateDirection()
                self.rect.x -= self.velocityX

    def createBullet(self, spriteGroup):
        if self.falling == False:
            for group in spriteGroup:
                group.add(Bullet([spriteGroup], self.rect.centerx, self.rect.centery,
                                 5, (BULLETSIZE, BULLETSIZE), self.typeElement, self.currentFacing))

    def setImage(self, image):
        self.image = pygame.transform.scale(image, (self.width, self.height))
        return self.image

    def animateDirection(self):
        currentTime = pygame.time.get_ticks()
        if currentTime - self.lastUpdate > self.animationSpeed:
            self.setImage(
                self.animations[self.currentFacing][self.currentFrame])
            self.currentFrame += 1
            if self.currentFrame == self.ammountOfFrames:
                self.currentFrame = 0
            self.lastUpdate = currentTime

    def update(self):
        self.moverAuto()

    def draw(self):
        self.screen.blit(self.image, self.rect)

    # @property
    # def __pos(self):
    #     return self.__pos

    # @__pos.setter
    # def setPos(self, value: tuple):
    #     self.rect.center = value

    # @__pos.deleter
    # def pos(self):
    #     del self.__pos
