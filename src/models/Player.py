
import math
import pygame
from Config import *
from colors import BLACK, BLUE, GREEN, RED
from spriteSheet import loadSprites


class Player(pygame.sprite.Sprite):

    def __init__(self, groups, x: int, y: int, width: int, height: int, screen: pygame.display) -> None:
        super().__init__(groups)
        self.groupsSprites = groups
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.lives = 3
        self.isAttacking = False
        self.currentFrame = 0
        self.currentFrameAttack = 0
        self.spriteKeys = ['down', 'rigth', 'left',
                           'dance', 'knee']
        self.sheet = PLAYERSHEET
        self.animations = loadSprites(
            self.sheet, SPIRTESIZEMAINWIDTH, SPIRTESIZEMAINHEIGHT, SPIRTEMAINROW, SPIRTEMAINCOL, self.spriteKeys)
        self.image = self.setImage(self.animations['down'][self.currentFrame])
        self.rect = self.image.get_rect(topleft=(x, y))

        self.attackImgsheet = loadImage('piña.png')
        self.animationsAttack = loadSprites(
            self.attackImgsheet, PLAYERWIDTH, PLAYERHEIGHT, 2, SPIRTEMAINCOL, ['right', 'left'])
        self.attackImg = self.animationsAttack['right'][self.currentFrameAttack]

        self.lastUpdateAttack = pygame.time.get_ticks()
        # self.Attackcooldown = 300
        # self.rect.center = (self.x, self.y)
        self.mask = pygame.mask.from_surface(self.image)

        self.screen = screen
        self.lastUpdate = pygame.time.get_ticks()
        self.lastUpdateVidas = pygame.time.get_ticks()

        # PLAYER MOVEMENT
        self.direction = pygame.math.Vector2(0, 0)
        self.falling = True
        self.dance = False
        self.shoot = False
        self.currentFacing = 'down'
        self.jumping = False
        self.gravity = 0.72
        self.jump_speed = -16.8
        # self.gravity = 0.1
        # self.jump_speed = -6.5
        self.onGround = True
        self.jumpCount = 0
        self.isKilled = False
        self.atackSprite = pygame.sprite.Group()
        self.isAttacking = False
        self.attacking_rect = pygame.Rect(
            self.rect.left, self.rect.top, PLAYERWIDTH, PLAYERHEIGHT)

    def setPlayerSpeed(self, speed=1.5):
        self.speedX = speed

    def setImage(self, image):
        image = pygame.transform.scale(image, (self.width, self.height))
        return image

    def getHit(self):
        currentTime = pygame.time.get_ticks()
        if self.lives > 1:
            if currentTime - self.lastUpdateVidas > ANIMATIONSPEED*5:
                self.lives -= 1
                self.lastUpdateVidas = currentTime
        else:
            self.isKilled = True

    def animateDirection(self, key: str):
        currentTime = pygame.time.get_ticks()
        if currentTime - self.lastUpdate > ANIMATIONSPEED:
            self.image = pygame.transform.scale(
                self.animations[key][self.currentFrame], (self.width, self.height))
            self.currentFrame += 1
            if self.currentFrame == SPIRTEMAINCOL:
                self.currentFrame = 0
            self.lastUpdate = currentTime

    def animateDirectionAttack(self, key: str):
        currentTime = pygame.time.get_ticks()
        if currentTime - self.lastUpdateAttack > 150:
            self.currentFrameAttack += 1
            if self.currentFrameAttack == 4:
                self.currentFrameAttack = 0
                # self.isAttacking = False
            self.attackImg = self.animationsAttack[key][self.currentFrameAttack]
            self.attackImg = pygame.transform.scale(
                self.attackImg, (self.width, self.height))
            self.lastUpdateAttack = currentTime

    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def jump(self):
        self.direction.y = self.jump_speed
        self.jumpCount += 1

    def attack(self, direction):
        if direction == 'rigth':
            self.attacking_rect = pygame.Rect(
                self.rect.right, self.rect.y, PLAYERWIDTH, PLAYERHEIGHT)
            self.animateDirectionAttack('right')
            self.screen.blit(self.attackImg, self.attacking_rect)
        if direction == 'left':
            self.attacking_rect = pygame.Rect(
                self.rect.left - PLAYERWIDTH, self.rect.y, PLAYERWIDTH, PLAYERHEIGHT)
            self.animateDirectionAttack('left')
            self.screen.blit(self.attackImg, self.attacking_rect)

    def get_inputs(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] == False:
            self.isAttacking = False

        if keys[pygame.K_s] == False:
            self.shoot = False

        if keys[pygame.K_SPACE]:
            self.attack(self.currentFacing)
            self.isAttacking = True
            self.direction.x = 0
            self.dance = False

        if keys[pygame.K_s]:
            self.shoot = True

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

        if keys[pygame.K_LSHIFT]:
            self.dance = True
        else:
            self.dance = False

    def update(self):
        if self.dance == True:
            self.animateDirection('dance')
        self.get_inputs()

    def draw(self):
        self.screen.blit(self.image, self.rect)
