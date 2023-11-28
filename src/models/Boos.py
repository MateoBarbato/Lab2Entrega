from random import randint
from tarfile import BLOCKSIZE
import pygame
from Config import BOOSSHEET, BULLETSIZE, ENEMYVELOCITY, GRAVITY, LIMITHEIGHTGROUND, LIMITWIDTHGROUND, SCREENHEIGHT, SCREENWIDTH, SPRITEBELLSPROUT, SPRITEBUGCOL, SPRITEBUGROW, SPRITEBUGSIZE, ANIMATIONSPEED, loadImage
from models.Bullet import Bullet

from spriteSheet import loadSprites


class Boss(pygame.sprite.Sprite):

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
        self.sheet = BOOSSHEET
        self.spriteKeys = ['idle']
        self.animations = loadSprites(
            self.sheet, 200, 93, 1, 8, self.spriteKeys)
        self.image = self.setImage(self.animations['idle'][self.currentFrame])
        self.rect = self.image.get_rect(topleft=(width,  height*2))
        self.mask = pygame.mask.from_surface(self.image)
        self.screen = screen
        self.lastUpdate = pygame.time.get_ticks()
        self.lastUpdateShooting = pygame.time.get_ticks()
        self.animationSpeed = ANIMATIONSPEED/1.5
        self.ammountOfFrames = 8
        self.currentFacing = 'idle'
        self.bullets = bulletsGroup
        self.falling = False

    def setImage(self, image):
        self.image = pygame.transform.scale(image, (self.width, self.height))
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

    def bulletHell(self):
        pass

    def update(self):
        self.animate()

    def draw(self):
        self.screen.blit(self.image, self.rect)
