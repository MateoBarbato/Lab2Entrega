from random import randint
import random
from re import S
import pygame
from Config import ANIMATIONSPEED, BACKGROUNDLEVEL1, BLOCKWIDTH, BUGSIZE, BULLETSIZE, ENEMYVELOCITY, GAMEMUSIC, LIVEUP, PLAYERHEIGHT, PLAYERWIDTH, SCREENHEIGHT, SCREENWIDTH, SHOOT, SPRITECANGREJO
from colors import BLACK
from helpers import createScreen, drawBackground, randIntPos
from models.Boos import Boss
from models.Bug import Bug
from models.BugsStatic import BugStatic
from models.Bullet import Bullet
from models.Counter import Counter
from models.Platform import Platform
from models.Player import Player
from models.Point import Point
from models.Lives import Live


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
        self.lastUpdateShootingPlayer = pygame.time.get_ticks()
        self.lastUpdateShootingBoss = pygame.time.get_ticks()
        self.lastUpdateLife = pygame.time.get_ticks()
        self.playerpickedLife = False
        self.playerGotHitted = False
        self.plataformas = pygame.sprite.Group()
        self.points = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self.playerbullets = pygame.sprite.Group()
        self.movingEnemies = pygame.sprite.Group()
        self.life = pygame.sprite.GroupSingle()
        self.player = pygame.sprite.GroupSingle()
        self.boss = pygame.sprite.GroupSingle()
        self.enemiesArray = []
        self.movingEnemiesArray = []
        self.timeTotal = 60
        self.timeForLife = 45
        self.scoreTotal = 0
        self.pointPerEnemy = 15
        self.levelDone = False
        self.music = GAMEMUSIC
        self.musicVolume = 0.5
        self.setUpVolume()
        self.setupLevel(self.spriteGroupAll, levelData)
        self.music.play(-1).set_volume(self.musicVolume)
        self.createCounter()

    def setUpVolume(self):
        if self.mute == True:
            self.musicVolume = 0.5
        else:
            self.musicVolume = 0

    def stopMusic(self):
        self.music.stop()

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
                elif celda == 'L':
                    self.life.add(
                        Live([spriteGroupAll, self.life], (x, y), BLOCKWIDTH))
                elif celda == 'B':
                    self.boss.add(
                        Boss([spriteGroupAll, self.boss], self.bullets, x, y, 400, 186, self.screen, 500))

        self.playerSprite = self.player.sprite
        self.lifeSprite = self.life.sprite
        self.bossSprite = self.boss.sprite

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

    def spawnLife(self):
        if len(self.life) <= 0:
            x = randint(0, 1)
            if x:
                xPos = 128
            else:
                xPos = 1024
            self.life.add(
                Live([self.spriteGroupAll, self.life], (xPos, 576), BLOCKWIDTH))
            self.timeForLife = int(self.timeForLife / 2)

    def createCounter(self):
        self.counter = Counter(
            self.scoreTotal, self.playerSprite.lives, self.screen, self.gameTime)

    def enemyShoots(self):
        currentTime = pygame.time.get_ticks()
        if currentTime - self.lastUpdateShooting > 1400:
            for enemy in self.enemies:
                enemy.shootSound()
                self.bullets.add(Bullet([self.spriteGroupAll, self.bullets], enemy.rect.centerx, enemy.rect.centery,
                                        5, (BULLETSIZE, BULLETSIZE), 'plant', enemy.currentFacing))
            for enemy in self.movingEnemies:
                enemy.shootSound()
                self.bullets.add(Bullet([self.spriteGroupAll, self.bullets], enemy.rect.centerx, enemy.rect.centery,
                                        5, (BULLETSIZE, BULLETSIZE), 'water', enemy.currentFacing))
            self.lastUpdateShooting = currentTime

    def playerShoots(self):
        currentTime = pygame.time.get_ticks()
        if currentTime - self.lastUpdateShootingPlayer > 650:
            if self.playerSprite.currentFacing != 'down' or None:
                self.playerSprite.shootSound()
                self.playerbullets.add(Bullet([self.spriteGroupAll, self.playerbullets], self.playerSprite.rect.centerx, self.playerSprite.rect.centery,
                                              7, (BULLETSIZE, BULLETSIZE), 'player', self.playerSprite.currentFacing))

                self.lastUpdateShootingPlayer = currentTime

    def bossShooting(self):
        currentTime = pygame.time.get_ticks()
        if self.timeTotal % 2 != 0:
            if currentTime - self.lastUpdateShootingBoss > 450:
                x = randint(0, 1)
                if x:
                    direction = 'rigth'
                    startPos = -64
                else:
                    direction = 'left'
                    startPos = SCREENWIDTH + 64
                self.bullets.add(Bullet([self.spriteGroupAll, self.bullets], startPos, (64/2)*randint(14, 24),
                                        10, (BULLETSIZE, BULLETSIZE), 'boss', direction))
                # self.bullets.add(Bullet([self.spriteGroupAll, self.bullets], startPos, (64/2)*randint(7, 12),
                #                         10, (BULLETSIZE, BULLETSIZE), 'boss', direction))
                self.lastUpdateShootingBoss = currentTime
        if self.timeTotal % 2 == 0:
            if currentTime - self.lastUpdateShootingBoss > 450:
                x = randint(0, 1)
                if x:
                    direction = 'down'
                    startPos = -64
                else:
                    direction = 'up'
                    startPos = SCREENHEIGHT + 64
                self.bullets.add(Bullet([self.spriteGroupAll, self.bullets],  (64/2)*randint(14, 34), startPos,
                                        10, (BULLETSIZE, BULLETSIZE), 'boss', direction))
                self.lastUpdateShootingBoss = currentTime

    def check_bullet_bounds(self, screenWidth):
        for bullet in self.bullets:
            if bullet.rect.right < -128 or bullet.rect.left > screenWidth+128:
                bullet.kill()
                self.scoreTotal += 5

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
                        plataforma.trapOn = True
                        if plataforma.currentFrame > 2:
                            currentTime = pygame.time.get_ticks()
                            if currentTime - self.lastUpdateLife > ANIMATIONSPEED*3:
                                plataforma.trapOn = False
                                self.lastUpdateLife = currentTime
                                plataforma.trapSound()
                                self.playerSprite.getHit()
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
                    if enemy.firstTimeFalling:
                        enemy.randDirection()
                        enemy.firstTimeFalling = False

    def horizontal_movement_colission_enemies(self, enemy):
        # MUEVO AL BICHO
        enemy.move()
        # chequeo colisiones horizontales
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

    def playerGetHitted(self):
        self.playerSprite.getHit()
        self.playerGotHitted = True

    def addLife(self):
        self.playerpickedLife = True
        self.playerSprite.liveUpSound()
        if self.playerSprite.lives < 3:

            self.playerSprite.lives += 1

    def timer(self):
        currentTime = pygame.time.get_ticks()
        if currentTime - self.gameTime > 1000:
            self.timeTotal -= 1
            self.gameTime = currentTime
            if self.playerpickedLife:
                self.playerpickedLife = False
            if self.playerGotHitted:
                self.playerGotHitted = False

    def run(self):
        self.timer()
        self.counter.updateLivesPlayer(self.playerSprite.lives)
        drawBackground(self.screen, self.background)
        self.counter.update(self.scoreTotal, self.timeTotal)
        self.enemyShoots()
        self.spriteGroupAll.update()
        self.spriteGroupAll.draw(self.screen)
        self.vertical_movement_colission()
        self.horizontal_movement_colission()

        if self.bossSprite:
            self.bossShooting()
            self.check_bullet_bounds(SCREENWIDTH)
            if self.timeTotal < self.timeForLife:
                self.spawnLife()

        if self.playerSprite.shoot == True:
            self.playerShoots()

        if self.playerSprite.isKilled or self.timeTotal == 0:
            self.levelDone = True

        if len(self.enemies) < 1 and len(self.movingEnemies) < 1 and len(self.boss) == 0:
            self.respawnEnemies()

        if pygame.sprite.spritecollide(self.playerSprite, self.life, True):
            if self.playerpickedLife == False:
                self.addLife()

        for enemy in self.enemies:
            self.vertical_movement_colission_enemies(enemy)

            if self.playerSprite.attacking_rect.colliderect(enemy):
                enemy.dyingSound()
                enemy.kill()

            colisionTrue = pygame.sprite.collide_mask(
                self.playerSprite, enemy)
            if colisionTrue:

                if self.playerSprite.isAttacking == True:
                    enemy.dyingSound()
                    enemy.kill()
                    self.scoreTotal += enemy.pointsToAdd
                else:
                    if self.playerGotHitted == False:
                        self.playerGetHitted()

        for enemy in self.movingEnemies:
            self.vertical_movement_colission_enemies(enemy)
            self.horizontal_movement_colission_enemies(enemy)

            if self.playerSprite.attacking_rect.colliderect(enemy) and self.playerSprite.isAttacking == True:
                enemy.dyingSound()
                enemy.kill()

            colisionTrue = pygame.sprite.collide_mask(
                self.playerSprite, enemy)
            if colisionTrue:

                if self.playerSprite.isAttacking == True:
                    enemy.dyingSound()
                    enemy.kill()
                    self.scoreTotal += enemy.pointsToAdd
                else:
                    if self.playerGotHitted == False:
                        self.playerGetHitted()

        for point in self.points:
            if pygame.sprite.collide_mask(self.playerSprite, point):
                self.scoreTotal += point.pointsToAdd
                point.addPointSound()
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
                            enemy.dyingSound()
                            enemy.kill()
                if len(self.movingEnemies) > 0:
                    for enemy in self.movingEnemies:
                        stateCollision2 = pygame.sprite.collide_mask(
                            bullet, enemy)

                        if stateCollision2:
                            bullet.isKilled = True
                            self.scoreTotal += enemy.pointsToAdd
                            enemy.dyingSound()
                            enemy.kill()

        if len(self.bullets) > 0:
            for bullet in self.bullets:
                if pygame.sprite.collide_mask(self.playerSprite, bullet):
                    if bullet.isKilled == False:

                        if self.playerGotHitted == False:
                            self.playerGetHitted()
                        bullet.isKilled = True

                if self.bossSprite == None:
                    if pygame.sprite.spritecollideany(
                            bullet, self.plataformas):
                        bullet.isKilled = True
