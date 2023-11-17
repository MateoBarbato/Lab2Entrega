from random import randint
from turtle import down
import pygame
from Config import SCREENHEIGHT, SCREENWIDTH, SPRITEBUGCOL, SPRITEBUGROW, SPRITEBUGSIZE, ANIMATIONSPEED, loadImage
from models.Bullet import Bullet
from spriteSheet import loadSprites


class BugStatic(pygame.sprite.Sprite):

    def __init__(self, groups, x: int, y: int, width: int, height: int, screen: pygame.display, imageSheet: str = None) -> None:
        super().__init__(groups)
        self.groupsVar = groups
        self.bugList = ['pokemon1.png', 'pokemon2.png', 'pokemon3.png']
        self.x = x
        self.y = y
        self.speed = 1
        self.pos = (x, y)
        self.width = width
        self.height = height
        self.currentFrame = 0
        if imageSheet:
            self.sheet = loadImage(imageSheet)
        else:
            self.imageIndex = randint(0, 2)
            self.sheet = loadImage(self.bugList[self.imageIndex])
        self.spriteKeys = ['down', 'rigth', 'left']
        self.animations = loadSprites(
            self.sheet, SPRITEBUGSIZE, SPRITEBUGSIZE, SPRITEBUGROW, SPRITEBUGCOL, self.spriteKeys)
        self.image = self.setImage(self.animations['down'][self.currentFrame])
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
        self.mask = pygame.mask.from_surface(self.image)
        self.screen = screen
        self.isBlited = False
        self.lastUpdate = pygame.time.get_ticks()
        self.animationSpeed = ANIMATIONSPEED
        self.ammountOfFrames = SPRITEBUGCOL
        self.currentFacing = 'left'
        # self.setRandomPos()
        self.bullets = []

    def setRandomPos(self):
        print(self.y)
        x = randint(0, SCREENWIDTH-self.width)
        y = self.y
        self.x = x
        self.y = y
        return (x, y)

    def delBug(self):
        del self

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
        # determino la direccion del sprite
        if self.x > SCREENWIDTH/2:
            self.animateDirection()
            self.currentFacing = 'left'
        else:
            self.animateDirection()
            self.currentFacing = 'rigth'
        # una vez se la direccion creo el disparo
        # self.shoot()

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
