import pygame
from Config import ANIMATIONSPEED, BLOCKWIDTH, BULLETPLANT, BULLETWATER, LIMITWIDTHGROUND, SCREENWIDTH, SPIRTESIZEMAINHEIGHT, SPIRTESIZEMAINWIDTH, SPRITEBUGCOL, loadImage

from spriteSheet import loadSprites


class Bullet(pygame.sprite.Sprite):
    def __init__(self, groups, x, y, speed, size, type, currentFacing) -> None:
        super().__init__(groups)
        self.x = x
        self.y = y
        self.size = size
        self.width = size[0]
        self.height = size[1]
        self.speed = speed
        self.currentFacing = currentFacing
        self.currentFrame = 0
        self.ammountOfFrames = SPRITEBUGCOL
        self.spriteKeys = ['left', 'rigth', 'dying']
        if type == 'plant':
            self.sheet = BULLETPLANT
            self.animations = loadSprites(
                self.sheet, 32, 32, 3, 4, self.spriteKeys)
        elif type == 'water':
            self.sheet = BULLETWATER
            self.animations = loadSprites(
                self.sheet, 32, 32, 3, 4, self.spriteKeys)
        elif type == 'player':
            self.sheet = BULLETWATER
            self.animations = loadSprites(
                self.sheet, 32, 32, 3, 4, self.spriteKeys)
        self.image = self.setImage(
            self.animations[self.currentFacing][self.currentFrame])
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        self.lastUpdate = pygame.time.get_ticks()
        self.lastUpdateKilling = pygame.time.get_ticks()
        self.loopAmmountKilling = 0
        self.animationSpeed = ANIMATIONSPEED
        self.isKilled = False

    def animateDirection(self, key: str):
        currentTime = pygame.time.get_ticks()
        if currentTime - self.lastUpdate > self.animationSpeed:
            self.setImage(self.animations[key][self.currentFrame])
            self.currentFrame += 1
            if self.currentFrame == self.ammountOfFrames:
                self.currentFrame = 0
            self.lastUpdate = currentTime

    def killanimated(self, key):
        self.currentFacing = 'dying'

        currentTime = pygame.time.get_ticks()
        if currentTime - self.lastUpdateKilling > 250:
            self.setImage(self.animations[key][self.currentFrame])
            self.currentFrame += 1
            self.rect.move_ip(0, 8)
            if self.currentFrame == self.ammountOfFrames:
                self.loopAmmountKilling = True
                self.currentFrame = 0
            self.lastUpdateKilling = currentTime
        if self.loopAmmountKilling == True:
            self.kill()

    def setImage(self, image):
        self.image = pygame.transform.scale(image, (self.width, self.height))
        return self.image

    def update(self):
        if self.isKilled == True:
            self.killanimated('dying')
        else:
            if self.currentFacing == 'left':
                if self.rect.x > BLOCKWIDTH:
                    self.rect.x += -self.speed
                    self.animateDirection('left')
                else:
                    self.isKilled = True

            if self.currentFacing == 'rigth':
                if self.rect.x < LIMITWIDTHGROUND - self.width:
                    self.rect.x += self.speed
                    self.animateDirection('rigth')
                else:
                    self.isKilled = True

    def draw(self):
        self.screen.blit(self.image, self.rect)
