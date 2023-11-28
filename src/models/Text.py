import os
import pygame

from colors import *


pygame.font.init()


class Text:
    """
    Represents a text object that can be rendered and blitted onto a pygame surface.

    Attributes:
        text (str): The text to display.
        color (pygame.Color): The color of the text.
        fontSize (int): The font size of the text.
        fontFamily (str): The font family of the text.
        font (pygame.Font): The pygame font object used to render the text.
        anitalisaing (bool): Whether to enable antialiasing for the text.

    Methods:
        setFontSize(size: int) -> None: Sets the font size of the text.
        setText(text: str) -> None: Sets the text to display.
        renderText() -> pygame.Surface: Renders the text onto a pygame surface.
        blitText(screen: pygame.Surface, coordinates: tuple, background: pygame.Color = LAVENDER, *borderRadius: int) -> None: Blits the rendered text onto the specified surface at the specified coordinates with an optional background and rounded corners.
        blitTextRect(screen: pygame.Surface, rectToBlit: pygame.Rect, background: pygame.Color = LAVENDER, *borderRadius: int) -> None: Blits the rendered text onto the specified surface within the specified rectangle with an optional background and rounded corners.
    """

    def __init__(self, text, color, fontSize, anitalisaing, fontFamily='Open Sans') -> None:
        """
        Initializes the Text object with the specified text, color, font size, and antialiasing.

        Args:
            text (str): The text to display.
            color (pygame.Color): The color of the text.
            fontSize (int): The font size of the text.
            anitalisaing (bool, optional): Whether to enable antialiasing for the text. Defaults to True.
            fontFamily (str, optional): The font family of the text. Defaults to 'Open Sans'.
        """
        self.text = text
        self.color = color
        self.fontSize = fontSize
        self.fontFamily = fontFamily
        self.font = pygame.font.Font(os.path.join(
            'assets', 'fonts', 'PixelifySans-VariableFont_wght.ttf'), self.fontSize)
        self.anitalisaing = anitalisaing

    def setFontSize(self, size=20):
        """
        Sets the font size of the text and updates the font object accordingly.

        Args:
            size (int, optional): The new font size. Defaults to 20.
        """
        self.font = pygame.font.Font(os.path.join(
            'assets', 'fonts', 'PixelifySans-VariableFont_wght.ttf'), size)

    def setText(self, text):
        """
        Sets the text to display and updates the rendered text surface accordingly.

        Args:
            text (str): The new text to display.
        """
        self.text = text

    def renderText(self):
        """
        Renders the current text onto a pygame surface and returns the surface.

        Returns:
            pygame.Surface: The rendered text surface.
        """
        text = self.font.render(self.text, self.antialias, self.color)

    def blitText(self, screen, coordinates: tuple, background=LAVENDER, *borderRadius):
        """
        Blits the rendered text onto the specified surface at the specified coordinates with an optional background and rounded corners.

        Args:
            screen (pygame.Surface): The surface to blit the text onto.
            coordinates (tuple): The (x, y) coordinates where to blit the text.
            background (pygame.Color, optional): The background color to draw behind the text. Defaults to LAVENDER.
            *borderRadius (int): The corner radius for rounded corners. Defaults to 0 (no rounded corners).
        """
        x, y = coordinates
        text = self.font.render(self.text, self.anitalisaing, self.color)
        textRect = text.get_rect()
        centerofRect = text.get_rect(
            center=(textRect.centerx, textRect.centery))
        centerofRect.left = x - textRect.width / 2
        centerofRect.top = y - textRect.height / 2
        screen.blit(text, centerofRect)

    def blitTextRect(self, screen, rectToBlit: pygame.Rect, background=LAVENDER, *borderRadius):
        """
        Blits the rendered text onto the specified surface within the specified rectangle with an optional background and rounded corners.

        Args:
            screen (pygame.Surface): The surface to blit the text onto.
            rectToBlit (pygame.Rect): The rectangle within which to blit the text.
            background (pygame.Color, optional): The background color to draw behind the text. Defaults to LAVENDER.
            *borderRadius (int): The corner radius for rounded corners. Defaults to 0 (no rounded corners).
        """
        text = self.font.render(self.text, True, self.color)
        centerofRect = text.get_rect(
            center=(rectToBlit.centerx, rectToBlit.centery))
        pygame.draw.rect(screen, background, rectToBlit, borderRadius)
        screen.blit(text, centerofRect)
