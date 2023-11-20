import pygame
from helpers import *
from Config import *
from colors import *
from models.Bug import Bug
from models.BugsStatic import BugStatic
from models.Bullet import Bullet
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
        self.shooterEnemy = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()

        self.animationSpeed = ANIMATIONSPEED
        self.player = Player([self.allSprites], SCREENWIDTH /
                             2, SCREENHEIGHT/2, PLAYERWIDTH, PLAYERHEIGHT, self.screen)
        # self.bug = Bug([self.shooterEnemy], randIntPos('x', 60),
        #                randIntPos('y', 60), BUGSIZE, BUGSIZE, self.screen)
        self.allSprites.add(Bug([self.allSprites], [self.bullets], randIntPos('x', 80), LIMITHEIGHTGROUND-BUGSIZE/2,
                                BUGSIZE, BUGSIZE, self.screen, 'pokemon4.png'))
        self.shooterEnemy.add(BugStatic([self.shooterEnemy], [self.bullets], randIntPos('x', 80), LIMITHEIGHTGROUND-BUGSIZE/2,
                                        BUGSIZE, BUGSIZE, self.screen, 'pokemon4.png'))
        self.muteState = mainMenu(self.screen, self.muteState)
        self.run()

    # def createBug():

    def run(self):
        self.gameRunning = True

        while self.gameRunning:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.quit()
                        exit()
                    if event.key == pygame.K_a:
                        self.player.control(-PLAYERVELOCITY, 0)
                        self.player.currentFacing = 'left'
                    if event.key == pygame.K_d:
                        self.player.control(PLAYERVELOCITY, 0)
                        self.player.currentFacing = 'rigth'
                    if event.key == pygame.K_w:
                        self.player.control(0, -(PLAYERVELOCITY))
                        self.player.jumping = True
                    if event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                        self.player.dance = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_a:
                        self.player.control(PLAYERVELOCITY, 0)
                        self.player.currentFacing = 'down'
                    if event.key == pygame.K_d:
                        self.player.control(-PLAYERVELOCITY, 0)
                        self.player.currentFacing = 'down'
                    if event.key == pygame.K_w:
                        self.player.control(0, PLAYERVELOCITY)
                        self.player.falling = True
                    if event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                        self.player.dance = False
            # BLIT Z
            if len(self.shooterEnemy) < 3:
                self.generateEnemiesRandom()

            if len(self.shooterEnemy) != 0:
                self.timedSequence()

            self.draw()

            pygame.display.flip()

    def generateEnemiesRandom(self):
        currentTime = pygame.time.get_ticks()
        if currentTime - self.lastUpdate > 1500:
            self.shooterEnemy.add(BugStatic([self.shooterEnemy], [self.bullets], randIntPos('x', 80), LIMITHEIGHTGROUND-BUGSIZE/2,
                                            BUGSIZE, BUGSIZE, self.screen, 'pokemon4.png'))
            self.lastUpdate = currentTime

    def timedSequence(self):
        currentTime = pygame.time.get_ticks()
        if currentTime - self.lastUpdateShooting > 2000:
            for bug in self.shooterEnemy:
                bug.createBullet(self.bullets)
            self.lastUpdateShooting = currentTime

    def draw(self):
        drawBackground(self.screen, BACKGROUNDLEVEL1)
        self.allSprites.draw(self.screen)
        self.shooterEnemy.draw(self.screen)
        self.bullets.draw(self.screen)

        # pygame.sprite.spritecollide(
        #     self.player, self.shooterEnemy, True)

        for bullet in self.bullets:
            bulletColisioned = pygame.sprite.collide_mask(self.player, bullet)
            if bulletColisioned:
                bullet.isKilled = True
        for enemy in self.shooterEnemy:
            colisionTrue = pygame.sprite.collide_mask(self.player, enemy)
            if colisionTrue:
                enemy.kill()
        # for bullet in self.bullets:
        #     pygame.sprite.spritecollide(
        #         bullet, self.shooterEnemy, True)

        self.allSprites.update()
        self.shooterEnemy.update()
        self.bullets.update()

    def quit(self):
        self.gameRunning = False
