import pygame
from helpers import *
from Config import *
from colors import *
from models.Bugs import Bug
from models.BugsStatic import BugStatic
from models.Bullet import Bullet
from models.Player import Player


class Game:

    def __init__(self) -> None:
        self.screen = createScreen()
        self.clock = pygame.time.Clock()
        self.clock.tick(60)
        self.lastUpdate = pygame.time.get_ticks()
        self.muteState = MUTESTATE
        self.bugs = []
        self.bugsStatic = []
        self.allSprites = pygame.sprite.Group()
        self.animationSpeed = ANIMATIONSPEED
        self.player = Player([self.allSprites], SCREENWIDTH /
                             2, SCREENHEIGHT/2, PLAYERWIDTH, PLAYERHEIGHT, self.screen)
        self.bug = Bug([self.allSprites], randIntPos('x', 60),
                       randIntPos('y', 60), BUGSIZE, BUGSIZE, self.screen)
        self.bugsStatic.append(BugStatic([self.allSprites], randIntPos('x', 80), LIMITHEIGHTGROUND-BUGSIZE/2,
                                         BUGSIZE, BUGSIZE, self.screen, 'pokemon4.png'))
        self.bullets = []
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
            # BLIT Z
            if len(self.bugs) < 8:
                self.generateEnemiesRandom()

            if self.bugsStatic != []:
                self.timedSequence()
            self.handleBullets()
            self.draw()

            pygame.display.flip()

    def generateEnemiesRandom(self):
        currentTime = pygame.time.get_ticks()
        if currentTime - self.lastUpdate > 10000:
            self.bugs.append(Bug([self.allSprites], randIntPos('x', BUGSIZE),
                                 randIntPos('y', BUGSIZE), BUGSIZE, BUGSIZE, self.screen))
            self.lastUpdate = currentTime

    def timedSequence(self):
        currentTime = pygame.time.get_ticks()
        if currentTime - self.lastUpdate > 3000:
            print('entre')
            for bug in self.bugsStatic[:]:
                self.bullets.append(Bullet([self.allSprites], bug.x, bug.y,
                                           3, (BULLETSIZE, BULLETSIZE), 'plant', bug.currentFacing))
            self.lastUpdate = currentTime

    def handleBullets(self):
        for bullet in self.bullets[:]:
            if bullet.x < 0:
                print('Fuera de pantalla izq')
                self.allSprites.remove(bullet)
            elif bullet.x > SCREENWIDTH:
                print('Fuera de pantalla der')
                self.allSprites.remove(bullet)

    def draw(self):
        drawBackground(self.screen, BACKGROUNDMAIN)
        self.allSprites.draw(self.screen)
        self.allSprites.update()

    def quit(self):
        self.gameRunning = False
