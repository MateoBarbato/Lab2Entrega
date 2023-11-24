from random import randint
import pygame
from Config import FRUIT1SHEET, FRUIT2SHEET, FRUIT3SHEET, SPRITEBUGSIZE

from spriteSheet import loadSprites


class Point(pygame.sprite.Sprite):
    def __init__(self, groups, pos, size) -> None:
        super().__init__(groups)
        self.size = size
        self.randoType()
        self.key = ['idle']
        self.isKilled = False
        # animaciones
        self.currentFacing = 'idle'
        self.currentFrame = 0
        self.animations = loadSprites(
            self.sheet, SPRITEBUGSIZE, SPRITEBUGSIZE, 1, 4, self.key)
        self.image = self.setImage(
            self.animations[self.currentFacing][self.currentFrame])
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(center=(pos[0]+size/2, pos[1]+size/2))
        self.lastUpdate = pygame.time.get_ticks()
        self.animationSpeed = 250
        self.ammountOfFrames = 4

    def setImage(self, image):
        self.image = pygame.transform.scale(
            image, (self.size/1.5, self.size/1.5))
        return self.image

    def randoType(self):
        self.randInt = randint(0, 2)
        if self.randInt == 0:
            self.sheet = FRUIT1SHEET
            self.type = 'red'
            self.pointsToAdd = 15
        elif self.randInt == 1:
            self.sheet = FRUIT2SHEET
            self.type = 'yellow'
            self.pointsToAdd = 25
        elif self.randInt == 2:
            self.sheet = FRUIT3SHEET
            self.type = 'blue'
            self.pointsToAdd = 35

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
        if self.isKilled:
            # hacer algo
            self.kill()
        self.animateDirection()
