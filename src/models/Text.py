import pygame

from colors import *


pygame.font.init()


class Text:

    def __init__(self, text, color, fontSize, anitalisaing, fontFamily='Open Sans') -> None:
        self.text = text
        self.color = color
        self.fontSize = fontSize
        self.fontFamily = fontFamily
        self.font = pygame.font.SysFont(self.fontFamily, fontSize)
        self.anitalisaing = anitalisaing

    def setFontSize(self, size=20):
        self.font = pygame.font.SysFont(self.fontFamily, size)

    def setText(self, text):
        self.text = text

    def renderText(self):
        text = self.font.render(self.text, self.antialias, self.color)

    def blitText(self, screen, coordinates: tuple, background=LAVENDER, *borderRadius):
        x, y = coordinates
        text = self.font.render(self.text, self.anitalisaing, self.color)
        textRect = text.get_rect()
        centerofRect = text.get_rect(
            center=(textRect.centerx, textRect.centery))
        centerofRect.left = x - textRect.width / 2
        centerofRect.top = y - textRect.height / 2
        screen.blit(text, centerofRect)

    def blitTextRect(self, screen, rectToBlit: pygame.Rect, background=LAVENDER, *borderRadius):
        text = self.font.render(self.text, True, self.color)
        centerofRect = text.get_rect(
            center=(rectToBlit.centerx, rectToBlit.centery))
        pygame.draw.rect(screen, background, rectToBlit, borderRadius)
        screen.blit(text, centerofRect)
