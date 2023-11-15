import pygame
from Config import *
from spriteSheet import loadSprites


class Player:

    def __init__(self, x: int, y: int, width: int, height: int, screen: pygame.display) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height
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
        self.speedY = 0
        self.speedX = 4
        self.firstTimeFalling = True
        self.ammountOfFrames = SPIRTEMAINCOL
        # self.velocityY = 0
        self.jumping = False
        self.lastUpdate = pygame.time.get_ticks()
        self.animationSpeed = 150

    def setPlayerSpeed(self, speed=1.5):
        self.speedX = speed

    def setImage(self, image):
        self.image = pygame.transform.scale(image, (self.width, self.height))
        return self.image

    def jump(self, state: bool):
        if state:
            self.speedY = -PLAYERVELOCITY
            self.jumping = True
            self.currentPos = self.rect.bottom
        else:
            self.jumping = False
            self.speedY = 0

    def animateDirection(self, key: str):
        currentTime = pygame.time.get_ticks()
        if currentTime - self.lastUpdate > self.animationSpeed:
            self.setImage(self.animations[key][self.currentFrame])
            self.currentFrame += 1
            if self.currentFrame == self.ammountOfFrames:
                self.currentFrame = 0
            self.lastUpdate = currentTime

    def update(self):

        key = pygame.key.get_pressed()
        if key[pygame.K_LSHIFT]:
            self.animateDirection('dance')
        if key[pygame.K_a]:
            if self.rect.left > 0:
                self.animateDirection('left')
                self.rect.move_ip(-self.speedX, 0)
        if key[pygame.K_d]:
            if self.rect.right < SCREENWIDTH:
                self.animateDirection('rigth')
                self.rect.move_ip(self.speedX, 0)
        else:
            if self.firstTimeFalling:
                self.animateDirection('knee')
            else:
                self.animateDirection('down')

        if self.jumping == False:
            if self.rect.bottom > SCREENHEIGHT-5:
                self.firstTimeFalling = False
                pass
            elif self.rect.bottom != SCREENHEIGHT:
                self.rect.move_ip(0, GRAVITY)
        if self.jumping == True:
            self.rect.move_ip(0, self.speedY)

    def blitPlayer(self):
        self.screen.blit(self.image, self.rect)
