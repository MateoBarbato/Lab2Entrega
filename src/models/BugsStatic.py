from random import randint
from tarfile import BLOCKSIZE
import pygame
from Config import BULLETSIZE, ENEMYVELOCITY, GRAVITY, LIMITHEIGHTGROUND, LIMITWIDTHGROUND, SCREENHEIGHT, SCREENWIDTH, SPRITEBELLSPROUT, SPRITEBUGCOL, SPRITEBUGROW, SPRITEBUGSIZE, ANIMATIONSPEED, loadImage
from models.Bullet import Bullet

from spriteSheet import loadSprites


class BugStatic(pygame.sprite.Sprite):

    def __init__(self, groups, bulletsGroup, x: int, y: int, width: int, height: int, screen: pygame.display, pointsToAdd: str) -> None:
        super().__init__(groups)
        self.x = x
        self.y = y
        self.speed = 1
        self.pos = (x, y)
        self.pointsToAdd = pointsToAdd
        self.width = width
        self.height = height
        self.currentFrame = 0
        self.sheet = SPRITEBELLSPROUT
        self.spriteKeys = ['down', 'rigth', 'left']
        self.animations = loadSprites(
            self.sheet, SPRITEBUGSIZE, SPRITEBUGSIZE, SPRITEBUGROW, SPRITEBUGCOL, self.spriteKeys)
        self.image = self.setImage(self.animations['down'][self.currentFrame])
        self.rect = self.image.get_rect(topleft=(x, y))
        self.mask = pygame.mask.from_surface(self.image)
        self.screen = screen
        self.lastUpdate = pygame.time.get_ticks()
        self.lastUpdateShooting = pygame.time.get_ticks()
        self.animationSpeed = ANIMATIONSPEED
        self.ammountOfFrames = SPRITEBUGCOL
        self.currentFacing = 'left'
        self.bullets = bulletsGroup
        self.falling = True
        self.velocityY = GRAVITY

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

        if self.falling:
            self.rect.y += self.velocityY

        # determino la direccion del sprite
        if self.x > LIMITWIDTHGROUND/2:
            self.animateDirection()
            self.currentFacing = 'left'
        else:
            self.animateDirection()
            self.currentFacing = 'rigth'

    def draw(self):
        self.screen.blit(self.image, self.rect)
