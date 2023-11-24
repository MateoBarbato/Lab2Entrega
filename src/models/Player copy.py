import math
import pygame
from Config import *
from spriteSheet import loadSprites


class Player(pygame.sprite.Sprite):

    def __init__(self, groups, x: int, y: int, width: int, height: int, screen: pygame.display) -> None:
        super().__init__(groups)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.movex = 0  # move along X
        self.movey = 0  # move along Y
        self.currentFrame = 0
        self.spriteKeys = ['down', 'rigth', 'left', 'dance', 'knee']
        self.sheet = loadImage('LucasSprite.png')
        self.animations = loadSprites(
            self.sheet, SPIRTESIZEMAINWIDTH, SPIRTESIZEMAINHEIGHT, SPIRTEMAINROW, SPIRTEMAINCOL, self.spriteKeys)
        self.image = self.setImage(self.animations['down'][self.currentFrame])
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        self.mask = pygame.mask.from_surface(self.image)
        self.screen = screen
        self.ammountOfFrames = SPIRTEMAINCOL
        self.lastUpdate = pygame.time.get_ticks()
        self.animationSpeed = ANIMATIONSPEED
        self.falling = True
        self.dance = False
        self.moving = True
        self.currentFacing = 'down'
        self.jumping = False
        self.distanceTotal = 0

    def setPlayerSpeed(self, speed=1.5):
        self.speedX = speed

    def setImage(self, image):
        self.image = pygame.transform.scale(image, (self.width, self.height))
        return self.image

    def animateDirection(self, key: str):
        currentTime = pygame.time.get_ticks()
        if currentTime - self.lastUpdate > self.animationSpeed:
            self.setImage(
                self.animations[key][self.currentFrame])
            self.currentFrame += 1
            if self.currentFrame == self.ammountOfFrames:
                self.currentFrame = 0
            self.lastUpdate = currentTime

    def control(self, x, y):
        """
        control player movement
        """
        self.movey += y
        self.movex += x

    def update(self):

        if self.dance == True:
            self.animateDirection('dance')
        else:
            self.animateDirection(self.currentFacing)
        if self.rect.left < BLOCKWIDTH:
            if self.movex > 0:
                self.rect.x = self.rect.x + self.movex
        elif self.rect.right > LIMITWIDTHGROUND:
            if self.movex < 0:
                self.rect.x = self.rect.x + self.movex
            self.movex = 0
        else:
            self.rect.x = self.rect.x + self.movex

        if self.falling == True:
                self.rect.y = self.rect.y + PLAYERVELOCITY*1.5
        elif self.jumping:
            self.distanceTotal += self.movey
            if self.distanceTotal < JUMPMAXHEIGH:
                self.jumping = False
                self.distanceTotal = 0
                self.falling = True
            else:
                self.rect.y = self.rect.y + self.movey

    def draw(self):
        self.screen.blit(self.image, self.rect)
