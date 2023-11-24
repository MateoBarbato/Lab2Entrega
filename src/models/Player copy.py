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
        self.lives = 3
        self.isAttacking = False

        self.currentFrame = 0
        self.spriteKeys = ['down', 'rigth', 'left',
                           'dance', 'knee', 'attackder', 'attackizq']
        self.sheet = PLAYERSHEETATTACK
        self.animations = loadSprites(
            self.sheet, SPIRTESIZEMAINWIDTH, SPIRTESIZEMAINHEIGHT, 7, SPIRTEMAINCOL, self.spriteKeys)
        self.image = self.setImage(self.animations['down'][self.currentFrame])
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        self.mask = pygame.mask.from_surface(self.image)
        self.screen = screen
        self.lastUpdate = pygame.time.get_ticks()
        self.lastUpdateVidas = pygame.time.get_ticks()
        # PLAYER MOVEMENT
        self.direction = pygame.math.Vector2(0, 0)
        self.falling = True
        self.dance = False
        self.moving = True
        self.currentFacing = 'down'
        self.jumping = False
        self.distanceTotal = 0
        self.gravity = 0.2
        self.jump_speed = -8.7
        # self.gravity = 0.1
        # self.jump_speed = -6.5
        self.onGround = True
        self.jumpCount = 0

        # 60 /s  64*3 1
    def setPlayerSpeed(self, speed=1.5):
        self.speedX = speed

    def setImage(self, image):
        self.image = pygame.transform.scale(image, (self.width, self.height))
        return self.image

    def getHit(self):
        currentTime = pygame.time.get_ticks()
        if self.lives > 0:
            if currentTime - self.lastUpdateVidas > ANIMATIONSPEED*4:
                self.lives -= 1
                print(self.lives)
                self.lastUpdateVidas = currentTime
        else:
            print('Matado')
            return True

        # def attack(self):
    #     print('asd')
    #     atackImg = pygame.Surface(
    #         (PLAYERWIDTH*3, PLAYERHEIGHT))
    #     attacking_Rect = atackImg.get_rect(
    #         center=(self.rect.centerx, self.rect.y,))
    #     self.screen.blit(self.image, attacking_Rect)

    def animateDirection(self, key: str):
        currentTime = pygame.time.get_ticks()
        if currentTime - self.lastUpdate > ANIMATIONSPEED/2:
            self.setImage(
                self.animations[key][self.currentFrame])
            self.currentFrame += 1
            if self.currentFrame == SPIRTEMAINCOL:
                self.currentFrame = 0
            self.lastUpdate = currentTime

    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def jump(self):
        self.direction.y = self.jump_speed
        self.jumpCount += 1

    def get_inputs(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE]:
            self.attack()
            self.isAttacking = True
        else:
            self.animateDirection(self.currentFacing)
            self.isAttacking = False

        if keys[pygame.K_d]:
            self.direction.x = PLAYERVELOCITY
            self.currentFacing = 'rigth'
            self.animateDirection('rigth')
        elif keys[pygame.K_a]:
            self.direction.x = -PLAYERVELOCITY
            self.currentFacing = 'left'
            self.animateDirection('left')
        else:
            self.direction.x = 0

        if keys[pygame.K_w] and self.onGround:
            if self.jumpCount < 2:
                self.jump()

    def update(self):
        if self.dance == True:
            self.animateDirection('dance')
        self.get_inputs()
        self.apply_gravity()

    def draw(self):
        self.screen.blit(self.image, self.rect)
