import pygame
from helpers import *
from Config import *
from colors import *
from models.Bug import Bug
from models.BugsStatic import BugStatic
from models.Bullet import Bullet
from models.Level import Level
from models.Platform import Platform
from models.Player import Player


class Game:

    def __init__(self) -> None:
        self.screen = createScreen()
        self.clock = pygame.time.Clock()
        self.clock.tick(60)
        self.lastUpdate = pygame.time.get_ticks()
        self.lastUpdateShooting = pygame.time.get_ticks()
        self.muteState = MUTESTATE
        self.allSprites = pygame.sprite.Group()

        self.level = Level(self.allSprites, level_map1,
                           BACKGROUNDLEVEL1, self.screen)
        self.gameRunning = True
        # self.bullets = pygame.sprite.Group()
        # self.plataformas = pygame.sprite.Group()
        # self.enemiesSprites = pygame.sprite.Group()
        # self.playerSprite = pygame.sprite.Group()
        # self.animationSpeed = ANIMATIONSPEED
        self.muteState = mainMenu(self.screen, self.muteState)
        self.run()

    # def createBug():

    def run(self):

        while self.gameRunning:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.quit()
                        exit()
            self.level.run()
            pygame.display.update()

    # def generateEnemiesRandom(self):
    #     currentTime = pygame.time.get_ticks()
    #     if currentTime - self.lastUpdate > 1500:
    #         if len(self.enemiesSprites) == 0:
    #             self.enemiesSprites.add(
    #                 Bug([self.allSprites, self.enemiesSprites], [self.bullets], randIntPos('x', 80), LIMITHEIGHTGROUND/2,
    #                     BUGSIZE, BUGSIZE, self.screen, 'water', SPRITECANGREJO),

    #                 BugStatic([self.enemiesSprites, self.allSprites], [self.bullets], 96, 600,
    #                           BUGSIZE, BUGSIZE, self.screen, 'pokemon4.png'),
    #                 BugStatic([self.enemiesSprites, self.allSprites], [self.bullets], 1110, 400,
    #                           BUGSIZE, BUGSIZE, self.screen, 'pokemon4.png')
    #             )
    #         self.lastUpdate = currentTime

    # def horizontal_movement_colission(self):
    #     player = self.player
    #     player.rect.x += player.direction.x

    #     for plataforma in self.plataformas:
    #         if plataforma.rect.colliderect(player.rect):
    #             if player.direction.x < 0:
    #                 player.rect.left = plataforma.rect.right
    #             elif player.direction.x > 0:
    #                 player.rect.right = plataforma.rect.left

    # def vertical_movement_colission(self):
    #     player = self.player
    #     player.apply_gravity()

    #     for plataforma in self.plataformas:
    #         if plataforma.rect.colliderect(player.rect):
    #             if player.direction.y > 0:
    #                 player.rect.bottom = plataforma.rect.top
    #                 player.direction.y = 0
    #                 player.onGround = True
    #                 player.jumpCount = 0
    #             elif player.direction.y < 0:
    #                 player.rect.top = plataforma.rect.bottom
    #                 player.direction.y = 0

    # def timedSequence(self):
    #     currentTime = pygame.time.get_ticks()
    #     if currentTime - self.lastUpdateShooting > 2000:
    #         if len(self.enemiesSprites) != 0:
    #             for bug in self.enemiesSprites:
    #                 bug.createBullet([self.bullets, self.allSprites])
    #             self.lastUpdateShooting = currentTime

    # def update(self):
    #     self.allSprites.update()
    #     self.vertical_movement_colission()
    #     self.horizontal_movement_colission()

    #     # BLIT Z

    #     self.generateEnemiesRandom()
    #     self.timedSequence()

    #     for enemy in self.enemiesSprites:
    #         plataformaONEnemies = pygame.sprite.spritecollideany(
    #             enemy, self.plataformas)
    #         if plataformaONEnemies:
    #             enemy.falling = False
    #         else:
    #             enemy.falling = True

    #     for bullet in self.bullets:
    #         bulletColisionedPlayer = pygame.sprite.collide_mask(
    #             self.player, bullet)
    #         bulletCollisionedWall = pygame.sprite.spritecollideany(
    #             bullet, self.plataformas)

    #         if bulletColisionedPlayer or bulletCollisionedWall:
    #             bullet.isKilled = True
    #         if bulletColisionedPlayer:
    #             gameState = self.player.getHit()
    #             if gameState:
    #                 self.gameRunning = False
    #     if len(self.points) != 0:
    #         for point in self.points:
    #             pointCollided = pygame.sprite.collide_mask(
    #                 self.player, point)
    #             if pointCollided:
    #                 point.isKilled = True
    #     else:
    #         print('Level Completed')

    #     for enemy in self.enemiesSprites:
    #         colisionTrue = pygame.sprite.collide_mask(self.player, enemy)
    #         if colisionTrue:

    #             if self.player.isAttacking == True:
    #                 enemy.kill()
    #             else:
    #                 enemy.kill()
    #                 self.player.lives -= 1

    # def draw(self):
    #     drawBackground(self.screen, BACKGROUNDLEVEL1)
    #     self.allSprites.draw(self.screen)

    # def quit(self):
    #     self.gameRunning = False
