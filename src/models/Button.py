import pygame
from colors import *
from Config import *

pygame.font.init()


class Button:
    """
    Class representing a button within the game.

    Attributes:
        colorbackground (Color): The color of the button's background.
        width (int): The width of the button.
        height (int): The height of the button.
        text (str): The text displayed on the button.
        x (int): The x-coordinate of the button's position.
        y (int): The y-coordinate of the button's position.
        font (pygame.font.Font): The font used to render the button's text.
        rect (pygame.Rect): The rectangle defining the button's position and size.
        screen (pygame.display): The game's screen.
        colorText (Color): The color of the button's text.

    Methods:
        drawRect(borderRadius: int): Draws the button's background with rounded corners.
        setText(newtext: str, *colorText: Color): Sets the button's text and optional text color.
        setFont(fontSize: int): Sets the font used to render the button's text.
        CreateButtonMenu(background: Color = LAVENDER, borderRadius: int = 10): Creates the button's appearance and text for the main menu.
        buttonPressed(): Checks whether the mouse is currently hovering over the button.
        getRect() -> pygame.Rect: Returns the button's rectangle.
    """

    def __init__(self, width, height, x, y, text, screen,  colorbackground=LAVENDER, colorText=BLACK, fontSize=20) -> None:
        """
        Initializes the button.

        Args:
            width (int): The width of the button.
            height (int): The height of the button.
            x (int): The x-coordinate of the button's position.
            y (int): The y-coordinate of the button's position.
            text (str): The text displayed on the button.
            screen (pygame.display): The game's screen.
            colorbackground (Color = LAVENDER): The optional background color of the button.
            colorText (Color = BLACK): The optional text color of the button.
            fontSize (int = 20): The optional font size of the button's text.
        """
        self.colorbackground = colorbackground
        self.width = width
        self.height = height
        self.text = text
        self.x = x
        self.y = y
        self.font = self.setFont(fontSize)
        self.rect: pygame.Rect = pygame.Rect(x, y, self.width, self.height)
        self.rect.centerx = x
        self.rect.centery = y
        self.screen: pygame.display = screen
        self.colorText = colorText

    def drawRect(self, borderRadius):
        """
        Draws the button's background with rounded corners.

        Args:
            borderRadius (int): The radius of the rounded corners.
        """
        pygame.draw.rect(self.screen, self.colorbackground,
                         self.rect, border_radius=borderRadius)
        pygame.display.flip()

    def setText(self, newtext, *colorText):
        """
        Sets the button's text and optional text color.

        Args:
            newtext (str): The new text to display on the button.
            *colorText (Color): The optional text color. If none is provided, the current text color is used.
        """
        self.text = newtext
        if colorText:
            self.colorText = colorText

    def setFont(self, fontSize):
        """
        Sets the font used to render the button's text.

        Args:
            fontSize (int): The new font size.
        """
        self.font = pygame.font.Font(
            os.path.join('assets', 'fonts', 'PixelifySans-VariableFont_wght.ttf'), fontSize)

    def CreateButtonMenu(self, background=LAVENDER, borderRadius=10):
        """
        Creates the button's appearance and text for the main menu.

        Args:
            background (Color = LAVENDER): The optional background color of the button.
            borderRadius (int = 10): The optional radius of the rounded corners.
        """
        self.setFont(35)
        text = self.font.render(self.text, False, self.colorText)
        centerOfRect = text.get_rect(
            center=(self.rect.centerx, self.rect.centery))
        self.drawRect(borderRadius)
        self.screen.blit(text, centerOfRect.topleft)

    def buttonPressed(self):
        """
        Checks whether the mouse is currently hovering over the button.

        Returns:
            bool: True if the mouse is hovering over the button, False otherwise.
        """
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos[0], pos[1]):
            return True
        else:
            return False

    @property
    def returnRect(self) -> pygame.Rect:
        """
        Returns the button's rectangle.

        Returns:
            pygame.Rect: The button's rectangle.
        """
        return self.rect
