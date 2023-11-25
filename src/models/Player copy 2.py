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
        self.spriteKeys = ['down', 'rigth', 'left',
                           'dance', 'knee', 'attackder', 'attackizq']
        self.sheet = PLAYERSHEETATTACK
        self.animations = loadSprites(
            self.sheet, SPIRTESIZEMAINWIDTH, SPIRTESIZEMAINHEIGHT, 7, SPIRTEMAINCOL, self.spriteKeys)
        self.image = self.setImage(self.animations['down'][self.currentFrame])
        self.rect = self.image.get_rect(topleft=(x, y))
        # self.rect.center = (self.x, self.y)
        self.mask = pygame.mask.from_surface(self.image)
        self.screen = screen
        self.lastUpdate = pygame.time.get_ticks()
        self.lastUpdateVidas = pygame.time.get_ticks()
        self.lastUpdateAttack = pygame.time.get_ticks()
        self.Attackcooldown = 300
        # PLAYER MOVEMENT
        self.direction = pygame.math.Vector2(0, 0)
        self.falling = True
        self.dance = False
        self.moving = True
        self.currentFacing = 'down'
        self.jumping = False
        self.distanceTotal = 0
        self.gravity = 0.72
        self.jump_speed = -16.8
        # self.gravity = 0.1
        # self.jump_speed = -6.5
        self.onGround = True
        self.jumpCount = 0
        # 60 /s  64*3 1
        # self.atackRightPos = (self.rect.right, self.rect.top)
        # self.atackLeftPos = (self.rect.left-PLAYERWIDTH, self.rect.top)
        self.atackSprite = pygame.sprite.Group()
        self.isAttacking = False
        # self.atackInstance = self.Attack(self.rect.topleft, self.screen)
        # self.rectAttackder = self.Attack(
        #     (self.rect.right, self.rect.top), self.screen)
        # self.rectAttackizq = self.Attack(
        #     (self.rect.left-PLAYERWIDTH, self.rect.top), self.screen)

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

    def attack(self):
        self.isAttacking = True
        if self.currentFacing == 'rigth':
            self.animateDirection('attackder')
            self.Attack(self.rect.topleft, self.screen, 'rigth')
            # self.atackInstance.attackMele('rigth')

        elif self.currentFacing == 'left':

            self.animateDirection('attackizq')
            self.Attack(self.rect.topleft, self.screen, 'left')
            # self.atackInstance.attackMele('rigth')

    def animateDirection(self, key: str):
        currentTime = pygame.time.get_ticks()
        if currentTime - self.lastUpdate > ANIMATIONSPEED:
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
            self.animateDirection('down')
            self.direction.x = 0

        if keys[pygame.K_w] and self.onGround:
            if self.jumpCount < 2:
                self.jump()

        if keys[pygame.K_LSHIFT]:
            self.dance = True
        else:
            self.dance = False

    def update(self):
        self.atackRightPos = (self.rect.right, self.rect.top)
        self.atackLeftPos = (self.rect.left-PLAYERWIDTH, self.rect.top)
        if self.dance == True:
            self.animateDirection('dance')
        self.get_inputs()

    def draw(self):
        self.screen.blit(self.image, self.rect)
        # self.atackSprite.draw(self.screen)
        self.atackInstance.draw(self.screen)

    class Attack(pygame.sprite.Sprite):

        def __init__(self, pos, screen, dir) -> None:
            pygame.sprite.Sprite.__init__(self)
            self.screen = screen
            # self.direction = direction
            self.image = pygame.transform.scale(
                SPRITECANGREJO, (PLAYERWIDTH, PLAYERHEIGHT), pygame.Surface((PLAYERWIDTH, PLAYERHEIGHT)))
            self.rectattack = self.image.get_rect(topleft=pos)
            self.attackMele(dir)

        def attackMele(self, dir):
            if dir == 'left':
                self.rectattack.centerx = self.rectattack.centerx - PLAYERWIDTH
            else:
                self.rectattack.centerx = self.rectattack.centerx + PLAYERWIDTH
            self.draw()

        def update(self):
            pass

        def updatePos(self):
            pass

        def draw(self):
            pygame.draw.rect(self.screen, GREEN, self.rectattack)
            # self.screen.blit(self.image, self.rect)
