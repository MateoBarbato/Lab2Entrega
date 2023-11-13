import pygame

from colors import *


pygame.font.init()
class Text:
    
    def __init__(self,text,color,fontSize,) -> None:
        self.text = text
        self.color = color
        self.fontSize = fontSize
        self.font = pygame.font.SysFont("monospace",fontSize)


    def setFontSize(self,size=20) :
        self.font = pygame.font.SysFont("monospace",size)

    def setText(self,text):
        self.text = text

    def blitText(self,screen,coordinates:tuple,color=BLACK,background=LAVENDER,*borderRadius):
        x,y = coordinates
        text = self.font.render(self.text,True,color)
        textRect = text.get_rect()
        centerofRect = text.get_rect(center=(textRect.centerx,textRect.centery))
        centerofRect.left = x - textRect.width /2
        centerofRect.top = y - textRect.height /2
        screen.blit(text,centerofRect)

    def blitTextRect(self,screen,rectToBlit:pygame.Rect,color=BLACK,background=LAVENDER,*borderRadius):
        text = self.font.render(self.text,True,color)
        centerofRect = text.get_rect(center=(rectToBlit.centerx,rectToBlit.centery))
        pygame.draw.rect(screen,background,rectToBlit,borderRadius)
        screen.blit(text,centerofRect)