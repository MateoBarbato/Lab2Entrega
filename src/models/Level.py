import pygame
from Config import BACKGROUNDLEVEL1, BLOCKWIDTH, PLAYERHEIGHT, PLAYERWIDTH
from colors import BLACK
from helpers import createScreen, drawBackground
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
        self.player = pygame.sprite.GroupSingle()
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
                    # generar enemigo static
                    pass
                elif celda == 'M':
                    # generar enemigo que se mueve
                    pass

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

    def run(self):
        self.screen.fill(BLACK)
        drawBackground(self.screen, self.background)
        # plataformas
        self.spriteGroupAll.update()
        self.spriteGroupAll.draw(self.screen)
        self.vertical_movement_colission()
        self.horizontal_movement_colission()
