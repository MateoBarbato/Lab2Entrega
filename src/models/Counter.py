import time
import pygame
from Config import CORAZON, SCREENWIDTH, loadImage
from colors import WHITE
from models.Text import Text


class Counter():
    """
    Class representing a counter for the game.

    Attributes:
        score (int): The current score.
        lives (int): The remaining number of lives.
        screen (pygame.Surface): The game's screen.
        pygameTime (float): The time in seconds since the game started.
        Leveltime (int): The time in milliseconds since the current level started.
        imgCorazon (pygame.Surface): The image of a heart, representing a life.

    Methods:
        draw(): Draws the current score and lives on the screen.
        calculateTime(): Calculates the time elapsed since the game started.
        drawLives(): Draws the remaining number of lives on the screen.
        updateLives(increase=0): Updates the remaining number of lives by the specified amount.
        update(scoreTotal, time): Updates the counter with the specified score and time.
    """

    def __init__(self, scoreOfLevel, lives, screen, pygameTime) -> None:
        """
        Initializes the counter.

        Args:
            scoreOfLevel (int): The initial score.
            lives (int): The initial number of lives.
            screen (pygame.Surface): The game's screen.
            pygameTime (float): The current time in seconds since the game started.
        """
        self.score = scoreOfLevel
        self.lives = lives
        self.screen = screen
        self.pygameTime = time.time()
        self.Leveltime = pygame.time.get_ticks()
        self.imgCorazon = CORAZON

    def draw(self):
        """
        Draws the current score and lives on the screen.
        """
        self.drawLives()
        Text(f'00:{self.time}', WHITE, 28, True).blitText(
            self.screen, (SCREENWIDTH/2, 80))
        x = Text(f'{self.score}', WHITE, 26, True)
        x.setFontSize(48)
        x.blitText(self.screen, (200, 80))

    def calculateTime(self):
        """
        Calculates the time elapsed since the game started.

        Returns:
            int: The time elapsed in seconds.
        """
        self.Leveltime = pygame.time.get_ticks()
        return int((self.pygameTime - self.pygameTime)/1000)

    def drawLives(self):
        """
        Draws the remaining number of lives on the screen.
        """
        if self.lives > 0:
            for i in range(self.lives):
                self.rectCorazon = self.imgCorazon.get_rect(
                    center=((SCREENWIDTH/2 + 200) + 80*i, 80))
                self.screen.blit(self.imgCorazon, self.rectCorazon)

    def updateLives(self, increase=0):
        """
        Updates the remaining number of lives by the specified amount.

        Args:
            increase (int = 0): The amount to increase or decrease the number of lives.
        """
        if increase:
            self.lives += 0
        else:
            self.lives -= 0

    def updateLivesPlayer(self, lives):
        self.lives = lives

    def update(self, scoreTotal, time):
        """
        Updates the counter with the specified score and time.

        Args:
            scoreTotal (int): The new score.
            time (int): The new time in seconds.
        """
        self.time = time
        self.score = scoreTotal
        self.draw()
