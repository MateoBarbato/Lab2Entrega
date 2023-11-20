import pygame
from colors import *
from Config import *

pygame.font.init()


class Button:
    def __init__(self, width, height, x, y, text, screen,  colorbackground=LAVENDER, colorText=BLACK, fontSize=20) -> None:

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
        pygame.draw.rect(self.screen, self.colorbackground,
                         self.rect, border_radius=borderRadius)
        pygame.display.flip()

    def setText(self,newtext,*colorText):

        self.text = newtext
        if colorText:
            self.colorText = colorText

    def setFont(self,fontSize):
        self.font = pygame.font.Font('assets/fonts/PixelifySans-VariableFont_wght.ttf',fontSize)

    def CreateButtonMenu(self, background=LAVENDER, borderRadius=10):
        self.setFont(35)
        text = self.font.render(self.text, False, self.colorText)
        centerOfRect = text.get_rect(center=(self.rect.centerx,self.rect.centery))
        self.drawRect(borderRadius)
        self.screen.blit(text, centerOfRect.topleft)

    def buttonPressed(self):
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos[0], pos[1]):
            return True
        else:
            return False

    @property
    def getRect(self) -> pygame.Rect:
        return self.rect
