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

    def setPlayerSpeed(self, speed=1.5):
        self.speedX = speed

    def setImage(self, image):
        self.image = pygame.transform.scale(image, (self.width, self.height))
        return self.image

    def animateDirection(self, key: str):
        currentTime = pygame.time.get_ticks()
        if currentTime - self.lastUpdate > self.animationSpeed:
            self.setImage(self.animations[key][self.currentFrame])
            self.currentFrame += 1
            if self.currentFrame == self.ammountOfFrames:
                self.currentFrame = 0
            self.lastUpdate = currentTime

    def control(self, x, y):
        """
        control player movement
        """
        self.movex += x
        self.movey += y

    def update(self):

        if self.dance == True:
            self.animateDirection('dance')

        self.rect.x = self.rect.x + self.movex

        if self.falling == True:
            if self.rect.bottom < LIMITHEIGHTGROUND:
                self.rect.y = self.rect.y + PLAYERVELOCITY*1.5
            else:
                self.falling = False
        else:
            self.rect.y = self.rect.y + self.movey

        # if key[pygame.K_LSHIFT]:
        #     self.animateDirection('dance')

        # if key[pygame.K_a]:
        #     if self.rect.left > 60:
        #         self.direction = 'left'
        #         self.animateDirection('left')
        #         self.rect.move_ip(-(self.speedX/1.5), 0)

        # if key[pygame.K_d]:
        #     if self.rect.right < LIMITWIDTHGROUND:
        #         self.direction = 'rigth'
        #         self.animateDirection('rigth')
        #         self.rect.move_ip(self.speedX, 0)

        # if key[pygame.K_w]:
        #     self.falling = False
        #     self.rect.move_ip(0, -self.speedY)

        # if key[pygame.K_w] == False:
        #     if self.firstTimeFalling:
        #         self.animateDirection('knee')
        #     else:
        #         self.animateDirection('down')
        #     # PLAYER TOCA EL PISO
        #     if self.rect.bottom > LIMITHEIGHTGROUND:
        #         self.direction = 'down'
        #         self.falling = False
        #         self.firstTimeFalling = False
        #     # Player Cayendo
        #     elif self.rect.bottom != LIMITHEIGHTGROUND:
        #         self.falling = True
        #         if self.direction == 'left':
        #             self.animateDirection('left')
        #             if self.rect.left > 0:
        #                 self.rect.move_ip(-(self.speedX/1.5), GRAVITY)
        #             else:
        #                 self.animateDirection('down')
        #                 self.rect.move_ip(0, GRAVITY)
        #         if self.direction == 'rigth':
        #             self.animateDirection('rigth')
        #             if self.rect.right < LIMITHEIGHTGROUND:
        #                 self.rect.move_ip(self.speedX, GRAVITY)
        #             else:
        #                 self.animateDirection('down')
        #                 self.rect.move_ip(0, GRAVITY)
        #         else:
        #             self.animateDirection('down')
        #             self.rect.move_ip(0, GRAVITY)

    def draw(self):
        self.screen.blit(self.image, self.rect)
