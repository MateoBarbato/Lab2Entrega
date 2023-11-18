from random import randint
from turtle import left
import pygame
from Config import LIMITHEIGHTGROUND, LIMITWIDTHGROUND, SCREENHEIGHT, SCREENWIDTH, SPRITEBUGCOL, SPRITEBUGROW, SPRITEBUGSIZE, ANIMATIONSPEED, loadImage
from spriteSheet import loadSprites


class Bug(pygame.sprite.Sprite):

    def __init__(self, groups, x: int, y: int, width: int, height: int, screen: pygame.display, imageSheet: str = None) -> None:
        super().__init__(groups)
        self.bugList = ['pokemon1.png', 'pokemon2.png', 'pokemon3.png']
        self.x = x
        self.y = y
        self.speed = 1
        self.__pos = (x, y)
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
        self.rect.center = (self.pos)
        self.mask = pygame.mask.from_surface(self.image)
        self.screen = screen
        self.isBlited = False
        self.lastUpdate = pygame.time.get_ticks()
        self.animationSpeed = ANIMATIONSPEED
        self.ammountOfFrames = SPRITEBUGCOL
        self.valueDir = randint(0, 1)
        if self.valueDir == 0:
            self.direction = 'left'
        else:
            self.direction = 'rigth'

    def setImage(self, image):
        self.image = pygame.transform.scale(image, (self.width, self.height))
        return self.image

    def animateDirection(self):
        currentTime = pygame.time.get_ticks()
        if currentTime - self.lastUpdate > self.animationSpeed:
            self.setImage(self.animations[self.direction][self.currentFrame])
            self.currentFrame += 1
            if self.currentFrame == self.ammountOfFrames:
                self.currentFrame = 0
            self.lastUpdate = currentTime

    def setRandomPos(self):
        newpos = (randint(0, LIMITWIDTHGROUND-self.width),
                  randint(0, LIMITHEIGHTGROUND-self.height))
        self.setpos(newpos)

    def update(self):
        if self.direction == 'left':
            if self.rect.left > 0:
                self.rect.move_ip(-self.speed, 0)
                self.animateDirection('left')
            else:
                self.direction = 'rigth'
        if self.direction == 'rigth':
            if self.rect.right < LIMITWIDTHGROUND-self.rect.width:
                self.rect.move_ip(self.speed, 0)
                self.animateDirection('rigth')
            else:
                self.direction = 'left'

    # def draw(self):
    #     self.screen.blit(self.image, self.rect)

    @property
    def pos(self):
        return self.__pos

    @pos.setter
    def setPos(self, value: tuple):
        self.rect.center = (value)

    @pos.deleter
    def pos(self):
        del self.__pos
