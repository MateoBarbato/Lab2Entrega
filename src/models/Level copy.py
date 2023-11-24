import pygame
from Config import BACKGROUNDLEVEL1, BLOCKWIDTH, PLAYERHEIGHT, PLAYERWIDTH
from helpers import createScreen
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
        self.setupLevel(self.spriteGroupAll, levelData)
        self.screen = screen

    def setupLevel(self, spriteGroupAll, levelData):
        self.plataformas = pygame.sprite.Group()
        self.points = pygame.sprite.Group()
        self.player = pygame.sprite.Group()
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
                        Player([spriteGroupAll, self.player], x, y, PLAYERWIDTH, PLAYERHEIGHT, screen))

    def run(self):
        # plataformas
        self.plataformas.draw(self.screen)

        # jugador
        self.player.draw(self.screen)
