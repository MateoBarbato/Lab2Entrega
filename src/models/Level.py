from random import randint
import pygame
from Config import ANIMATIONSPEED, BACKGROUNDLEVEL1, BLOCKWIDTH, BUGSIZE, BULLETSIZE, ENEMYVELOCITY, PLAYERHEIGHT, PLAYERWIDTH, SPRITECANGREJO
from colors import BLACK
from helpers import createScreen, drawBackground, randIntPos
from models.Bug import Bug
from models.BugsStatic import BugStatic
from models.Bullet import Bullet
from models.Counter import Counter
from models.Platform import Platform
from models.Player import Player
from models.Point import Point


class Level:
    def __init__(self, levelData, background, screen, muteState) -> None:
        self.screen = createScreen()
        self.clock = pygame.time.Clock()
        self.clock.tick(60)
        self.spriteGroupAll = pygame.sprite.Group()
        self.levelData = levelData
        self.background = background
        self.screen = screen
        # timings
        self.mute = muteState
        self.delayRespawn = pygame.time.get_ticks()
        self.gameTime = pygame.time.get_ticks()
        self.lastUpdate = pygame.time.get_ticks()
        self.lastUpdateShooting = pygame.time.get_ticks()
        self.lastUpdateVidas = pygame.time.get_ticks()

        self.plataformas = pygame.sprite.Group()
        self.points = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self.playerbullets = pygame.sprite.Group()
        self.movingEnemies = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        self.enemiesArray = []
        self.movingEnemiesArray = []
        self.timeTotal = 60
        self.scoreTotal = 0
        self.pointPerEnemy = 15
        self.levelDone = False
        self.setupLevel(self.spriteGroupAll, levelData)
        self.createCounter()

    def muteHandler(self, muteValue):
        self.muteHandler = not self.muteHandler

    def getMuteValue(self):
        return self.muteHandler

    def setupLevel(self, spriteGroupAll, levelData, spawnPlayer=True):

        for rowIndex, row in enumerate(levelData):
            for colIndex, celda in enumerate(row):
                x = colIndex * BLOCKWIDTH
                y = rowIndex * BLOCKWIDTH
                if celda == '1' and spawnPlayer == True:
                    self.plataformas.add(
                        Platform([spriteGroupAll, self.plataformas], (x, y), BLOCKWIDTH, self.screen))
                if celda == '2' and spawnPlayer == True:
                    self.plataformas.add(
                        Platform([spriteGroupAll, self.plataformas], (x, y), BLOCKWIDTH, self.screen, True))
                elif celda == 'P' and spawnPlayer == True:
                    self.points.add(
                        Point([spriteGroupAll, self.points], (x, y), BLOCKWIDTH))
                elif celda == 'J' and spawnPlayer == True:
                    self.player.add(
                        Player([spriteGroupAll, self.player], x, y, PLAYERWIDTH, PLAYERHEIGHT, self.screen))
                elif celda == 'S':
                    self.enemies.add(
                        BugStatic([spriteGroupAll], [self.bullets], x, y,
                                  BUGSIZE, BUGSIZE, self.screen, self.pointPerEnemy))
                elif celda == 'M':
                    self.movingEnemies.add(Bug([spriteGroupAll, self.movingEnemies], [self.bullets], x, y,
                                               BUGSIZE, BUGSIZE, self.screen, 'water', SPRITECANGREJO, self.pointPerEnemy*2))
        self.playerSprite = self.player.sprite

    def respawnEnemies(self):
        for i in range(1):
            if i == 0:
                self.enemies.add(
                    BugStatic([self.spriteGroupAll], [self.bullets], randIntPos('x', 64), 320,
                              BUGSIZE, BUGSIZE, self.screen, self.pointPerEnemy))

                self.movingEnemies.add(Bug([self.spriteGroupAll, self.movingEnemies], [self.bullets], randIntPos('x', 64), 320,
                                           BUGSIZE, BUGSIZE, self.screen, 'water', SPRITECANGREJO, self.pointPerEnemy*2))
            elif i == 1:
                self.enemies.add(
                    BugStatic([self.spriteGroupAll], [self.bullets], randIntPos('x', 64), 320,
                              BUGSIZE, BUGSIZE, self.screen, self.pointPerEnemy))

                self.movingEnemies.add(Bug([self.spriteGroupAll, self.movingEnemies], [self.bullets], randIntPos('x', 64), 320,
                                           BUGSIZE, BUGSIZE, self.screen, 'water', SPRITECANGREJO, self.pointPerEnemy*2))

    def createCounter(self):
        self.counter = Counter(
            self.scoreTotal, self.playerSprite.lives, self.screen, self.gameTime)

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

    def playerShoots(self):
        currentTime = pygame.time.get_ticks()
        if currentTime - self.lastUpdateShooting > 650:
            if self.playerSprite.currentFacing != 'down' or None:
                self.playerbullets.add(Bullet([self.spriteGroupAll, self.playerbullets], self.playerSprite.rect.centerx, self.playerSprite.rect.centery,
                                              7, (BULLETSIZE, BULLETSIZE), 'plant', self.playerSprite.currentFacing))

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
        player = self.playerSprite
        player.apply_gravity()

        for plataforma in self.plataformas:
            if plataforma.rect.colliderect(player.rect):
                if player.direction.y > 0:
                    player.rect.bottom = plataforma.rect.top
                    player.direction.y = 0
                    player.onGround = True
                    player.jumpCount = 0
                    if plataforma.isTrap == True:
                        if plataforma.trapOn == False:
                            plataforma.trapOn = True
                        if plataforma.currentFrame > 2:
                            currentTime = pygame.time.get_ticks()
                            self.playerSprite.getHit()
                            if currentTime - self.lastUpdateVidas > ANIMATIONSPEED*4:
                                self.counter.updateLives()
                                self.lastUpdateVidas = currentTime
                elif player.direction.y < 0:
                    player.rect.top = plataforma.rect.bottom
                    player.direction.y = 0

    def vertical_movement_colission_enemies(self, enemy):
        enemy.apply_gravity()
        for plataforma in self.plataformas:
            if plataforma.rect.colliderect(enemy.rect):
                if enemy.direction.y > 0:
                    enemy.rect.bottom = plataforma.rect.top
                    enemy.direction.y = 0
                    enemy.randDirection()

    def horizontal_movement_colission_enemies(self, enemy):
        enemy.rect.x += enemy.direction.x

        for plataforma in self.plataformas:
            if plataforma.rect.colliderect(enemy.rect):
                if enemy.direction.x < 0:
                    enemy.rect.left = plataforma.rect.right
                    enemy.currentFacing = 'rigth'
                    enemy.direction.x = ENEMYVELOCITY
                elif enemy.direction.x > 0:
                    enemy.rect.right = plataforma.rect.left
                    enemy.direction.x = -ENEMYVELOCITY
                    enemy.currentFacing = 'left'

    def timer(self):
        currentTime = pygame.time.get_ticks()
        if currentTime - self.gameTime > 1000:
            self.timeTotal -= 1
            self.gameTime = currentTime

    def run(self):
        self.timer()
        drawBackground(self.screen, self.background)
        self.counter.update(self.scoreTotal, self.timeTotal)
        self.enemyShoots()
        self.spriteGroupAll.update()
        self.spriteGroupAll.draw(self.screen)
        self.vertical_movement_colission()
        self.horizontal_movement_colission()

        if self.playerSprite.shoot == True:
            self.playerShoots()

        if self.playerSprite.isKilled or self.timeTotal == 0:
            self.levelDone = True

        if len(self.enemies) < 1 and len(self.movingEnemies) < 1:
            self.respawnEnemies()

        for enemy in self.enemies:
            self.vertical_movement_colission_enemies(enemy)

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
                        self.counter.updateLives()
                        self.lastUpdateVidas = currentTime

        for enemy in self.movingEnemies:
            self.vertical_movement_colission_enemies(enemy)
            self.horizontal_movement_colission_enemies(enemy)

            if self.playerSprite.attacking_rect.colliderect(enemy) and self.playerSprite.isAttacking == True:
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
                        self.counter.updateLives()
                        enemy.kill()
                        self.lastUpdateVidas = currentTime

        for point in self.points:
            if pygame.sprite.collide_mask(self.playerSprite, point):
                self.scoreTotal += point.pointsToAdd
                point.kill()

        if len(self.playerbullets) > 0:
            for bullet in self.playerbullets:

                if pygame.sprite.spritecollideany(
                        bullet, self.plataformas):
                    bullet.isKilled = True

                if len(self.enemies) > 0:
                    for enemy in self.enemies:
                        stateCollision = pygame.sprite.collide_mask(
                            bullet, enemy)

                        if stateCollision:
                            bullet.isKilled = True
                            self.scoreTotal += enemy.pointsToAdd
                            enemy.kill()
                if len(self.movingEnemies) > 0:
                    for enemy in self.movingEnemies:
                        stateCollision2 = pygame.sprite.collide_mask(
                            bullet, enemy)

                        if stateCollision2:
                            bullet.isKilled = True
                            self.scoreTotal += enemy.pointsToAdd
                            enemy.kill()

        if len(self.bullets) > 0:
            for bullet in self.bullets:
                if pygame.sprite.collide_mask(self.playerSprite, bullet):
                    if bullet.isKilled == False:
                        print(self.playerSprite.lives)
                        self.playerSprite.getHit()
                        self.counter.updateLives()
                        bullet.isKilled = True

                if pygame.sprite.spritecollideany(
                        bullet, self.plataformas):
                    bullet.isKilled = True


# ALTERNATIVA SIN USAR DOBLE FOR PERO NO PODRIA HACER EL DOKILL  ANIMADO
        # if len(self.playerbullets) > 0:
        #     stateCollision = pygame.sprite.groupcollide(
        #         self.playerbullets, self.enemies, True, True)
        #     stateCollision2 = pygame.sprite.groupcollide(
        #         self.playerbullets, self.movingEnemies, True, True)
        #     if stateCollision:
        #         self.scoreTotal += enemy.pointsToAdd
        #     if stateCollision2:
        #         self.scoreTotal += enemy.pointsToAdd
