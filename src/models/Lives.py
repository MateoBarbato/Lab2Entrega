
from random import randint
import pygame
from Config import SPRITEBUGSIZE, VIDAPOINT

from spriteSheet import loadSprites


class Live(pygame.sprite.Sprite):
    def __init__(self, groups, pos, size) -> None:
        super().__init__(groups)
        self.size = size
        self.key = ['idle']
        self.isKilled = False
        # animaciones
        self.currentFacing = 'idle'
        self.currentFrame = 0
        self.sheet = VIDAPOINT
        self.animations = loadSprites(
            self.sheet, SPRITEBUGSIZE, SPRITEBUGSIZE, 1, 4, self.key)
        self.image = self.setImage(
            self.animations[self.currentFacing][self.currentFrame])
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(center=(pos[0]+size/2, pos[1]+size/2))
        self.lastUpdate = pygame.time.get_ticks()
        self.animationSpeed = 250
        self.ammountOfFrames = 4
        self.lifesToAdd = 1

    def setImage(self, image):
        self.image = pygame.transform.scale(
            image, (self.size/1.5, self.size/1.5))
        return self.image

    def animate(self):
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
        self.animate()
