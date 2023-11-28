import time
import pygame
from Config import CORAZON, SCREENWIDTH, loadImage
from colors import WHITE
from models.Text import Text


class Counter():
    def __init__(self, scoreOfLevel, lives, screen, pygameTime) -> None:
        self.score = scoreOfLevel
        self.lives = lives
        self.screen = screen
        self.pygameTime = time.time()
        self.Leveltime = pygame.time.get_ticks()
        self.imgCorazon = CORAZON

    def draw(self):
        self.drawLives()
        Text(f'00:{self.time}', WHITE, 28, True).blitText(
            self.screen, (SCREENWIDTH/2, 80))
        x = Text(f'{self.score}', WHITE, 26, True)
        x.setFontSize(48)
        x.blitText(self.screen, (200, 80))

    def calculateTime(self):
        self.Leveltime = pygame.time.get_ticks()
        return int((self.pygameTime - self.pygameTime)/1000)

    def drawLives(self):
        if self.lives > 0:
            for i in range(self.lives):
                self.rectCorazon = self.imgCorazon.get_rect(
                    center=((SCREENWIDTH/2 + 200) + 80*i, 80))
                self.screen.blit(self.imgCorazon, self.rectCorazon)

    def updateLives(self):
        self.lives -= 1

    def restart(self):
        self.pygameTime = pygame.time.get_ticks()
        self.time = 0

    def update(self, scoreTotal, time):
        self.time = time
        self.score = scoreTotal
        self.draw()
