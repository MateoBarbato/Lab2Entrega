import pygame
from Config import ANIMATIONSPEED, BACKGROUNDLEVEL1, BLOCKWIDTH, BUGSIZE, BULLETSIZE, PLAYERHEIGHT, PLAYERWIDTH, SPRITECANGREJO
from colors import BLACK
from helpers import createScreen, drawBackground
from models.Bug import Bug
from models.BugsStatic import BugStatic
from models.Bullet import Bullet
from models.Platform import Platform
from models.Player import Player
from models.Point import Point


class Level:
    def __init__(self, levelData, background, screen) -> None:
        self.screen = createScreen()
        self.clock = pygame.time.Clock()
        self.clock.tick(60)
        self.spriteGroupAll = pygame.sprite.Group()
        self.background = background
        self.screen = screen
        # timings

        self.lastUpdate = pygame.time.get_ticks()
        self.lastUpdateShooting = pygame.time.get_ticks()
        self.lastUpdateVidas = pygame.time.get_ticks()

        self.plataformas = pygame.sprite.Group()
        self.points = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self.movingEnemies = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()

        self.scoreTotal = 0
        self.pointPerEnemy = 15
        self.levelDone = False
        self.setupLevel(self.spriteGroupAll, levelData)

    def setupLevel(self, spriteGroupAll, levelData):

        for rowIndex, row in enumerate(levelData):
            for colIndex, celda in enumerate(row):
                x = colIndex * BLOCKWIDTH
                y = rowIndex * BLOCKWIDTH
                if celda == '1':
                    self.plataformas.add(
                        Platform([spriteGroupAll, self.plataformas], (x, y), BLOCKWIDTH))
                elif celda == 'P':
                    self.points.add(
                        Point([spriteGroupAll, self.points], (x, y), BLOCKWIDTH))
                elif celda == 'J':
                    self.player.add(
                        Player([spriteGroupAll, self.player], x, y, PLAYERWIDTH, PLAYERHEIGHT, self.screen))
                elif celda == 'S':
                    self.enemies.add(
                        BugStatic([spriteGroupAll], [self.bullets], x, y,
                                  BUGSIZE, BUGSIZE, self.screen, self.pointPerEnemy))
                elif celda == 'M':
                    self.movingEnemies.add(Bug([spriteGroupAll, self.movingEnemies], [self.bullets], x, y,
                                               BUGSIZE, BUGSIZE, self.screen, 'water', SPRITECANGREJO))
        self.playerSprite = self.player.sprite

    def enemyShoots(self):
        currentTime = pygame.time.get_ticks()
        if currentTime - self.lastUpdateShooting > 1800:
            for enemy in self.enemies:
                self.bullets.add(Bullet([self.spriteGroupAll, self.bullets], enemy.rect.centerx, enemy.rect.centery,
                                        5, (BULLETSIZE, BULLETSIZE), 'plant', enemy.currentFacing))
            for enemy in self.movingEnemies:
                self.bullets.add(Bullet([self.spriteGroupAll, self.bullets], enemy.rect.centerx, enemy.rect.centery,
                                        5, (BULLETSIZE, BULLETSIZE), 'water', enemy.currentFacing))
            self.lastUpdateShooting = currentTime

    def horizontal_movement_colission(self):
        player = self.player.sprite
        player.rect.x += player.direction.x

        for plataforma in self.plataformas:
            if plataforma.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = plataforma.rect.right
                elif player.direction.x > 0:
                    player.rect.right = plataforma.rect.left

    def vertical_movement_colission(self):
        player = self.player.sprite
        player.apply_gravity()

        for plataforma in self.plataformas:
            if plataforma.rect.colliderect(player.rect):
                if player.direction.y > 0:
                    player.rect.bottom = plataforma.rect.top
                    player.direction.y = 0
                    player.onGround = True
                    player.jumpCount = 0
                elif player.direction.y < 0:
                    player.rect.top = plataforma.rect.bottom
                    player.direction.y = 0

    def vertical_movement_colission_enemies(self, enemy):
        enemy = enemy
        for plataforma in self.plataformas:
            if plataforma.rect.colliderect(enemy.rect):
                if enemy.velocityY > 0:
                    enemy.rect.bottom = plataforma.rect.top
                    enemy.velocityY = 0
                elif enemy.velocityY < 0:
                    enemy.rect.top = plataforma.rect.bottom
                    enemy.velocityY = 0

    def run(self):
        drawBackground(self.screen, self.background)
        # plataformas
        self.enemyShoots()
        self.spriteGroupAll.update()
        self.spriteGroupAll.draw(self.screen)
        self.vertical_movement_colission()
        self.horizontal_movement_colission()

        if self.playerSprite.isKilled:
            self.levelDone = True

        for enemy in self.enemies:
            self.vertical_movement_colission_enemies(enemy)

        for point in self.points:
            if pygame.sprite.collide_mask(self.playerSprite, point):
                self.scoreTotal += point.pointsToAdd
                point.kill()

        if len(self.bullets) > 0:
            for bullet in self.bullets:
                if pygame.sprite.collide_mask(self.playerSprite, bullet):
                    if bullet.isKilled == False:
                        print(self.playerSprite.lives)
                        self.playerSprite.getHit()
                        bullet.isKilled = True

                if pygame.sprite.spritecollideany(
                        bullet, self.plataformas):
                    bullet.isKilled = True
        for enemy in self.enemies:
            # if self.playerSprite.isAttacking:
            if self.playerSprite.attacking_rect.colliderect(enemy):
                enemy.kill()

            colisionTrue = pygame.sprite.collide_mask(
                self.playerSprite, enemy)
            if colisionTrue:

                if self.playerSprite.isAttacking == True:
                    enemy.kill()
                    self.scoreTotal += enemy.pointsToAdd
                else:
                    currentTime = pygame.time.get_ticks()
                    if currentTime - self.lastUpdateVidas > ANIMATIONSPEED*4:
                        self.playerSprite.getHit()
                        # enemy.kill()
                        self.lastUpdateVidas = currentTime
