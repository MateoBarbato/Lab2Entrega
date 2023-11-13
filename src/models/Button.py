import pygame
from colors import *
from Config import *

pygame.font.init()
class Button:
    def __init__(self,color,width,height,x,y,text,screen) -> None:
        self.color = color
        self.width = width
        self.height = height
        self.text = text
        self.x = x
        self.y = y
        self.font = self.setFontSize(20)
        self.rect : pygame.Rect = pygame.Rect(x,y,self.width,self.height)
        self.rect.centerx = x
        self.rect.centery = y
        self.screen : pygame.display = screen

    def drawRect(self,color,screen):
        pygame.draw.rect(screen,color,self.rect)
        pygame.display.flip()

    def setFontSize(self,size=20) :
        self.font = pygame.font.SysFont("monospace",size)
    
    def CreateButtonMenu(self,screen,colorText=BLACK,background=LAVENDER,borderRadius=5):
        self.setFontSize(35)
        text = self.font.render(self.text,False,colorText)
        centerOfRect = text.get_rect(center=(self.rect.centerx,self.rect.centery))
        pygame.draw.rect(screen,background,self.rect,border_radius=borderRadius)
        screen.blit(text,centerOfRect)


    def buttonPressed (self):
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos[0],pos[1]):
            return True
        else:
            return False


    @property 
    def getRect(self) -> pygame.Rect:
        return self.rect
