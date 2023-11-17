import pygame
from helpers import *
from Config import *
from colors import *
from models.Bugs import Bug
from models.Player import Player


class Game:

    def __init__(self) -> None:
        self.screen = createScreen()
        self.clock = pygame.time.Clock()
        self.clock.tick(60)
        self.lastUpdate = pygame.time.get_ticks()
        self.muteState = MUTESTATE
        self.bugs = []
        self.allSprites = pygame.sprite.Group()
        self.player = Player([self.allSprites], SCREENWIDTH /
                             2, SCREENHEIGHT/2, 60, 80, self.screen)
        self.bug = Bug([self.allSprites], randIntPos('x', 60),
                       randIntPos('y', 60), 60, 60, self.screen)
        self.muteState = mainMenu(self.screen, self.muteState)
        self.run()

    # def createBug():

    def run(self):
        self.gameRunning = True
        background = loadBackground('fondo.png')
        while self.gameRunning:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.quit()
                        exit()
            # BLIT ZONE
            drawBackground(self.screen, background)
            self.generateEnemiesRandom()
            self.draw()

            pygame.display.flip()

    def generateEnemiesRandom(self):

        currentTime = pygame.time.get_ticks()
        if currentTime - self.lastUpdate > 10000:
            self.bugs.append(Bug([self.allSprites], randIntPos('x', 60),
                                 randIntPos('y', 60), 60, 60, self.screen))
            self.lastUpdate = currentTime

    def draw(self):

        self.allSprites.draw(self.screen)
        self.allSprites.update()

    def quit(self):
        self.gameRunning = False
