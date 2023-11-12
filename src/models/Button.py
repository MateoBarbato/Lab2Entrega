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
        self.screen : pygame.display = screen

    def drawRect(self,color,screen):
        pygame.draw.rect(screen,color,self.rect)
        pygame.display.flip()

    def setFontSize(self,size=20) :
        self.font = pygame.font.SysFont("monospace",size)
    
    def CreateButtonMenu(self,screen,color=BLACK,background=LAVENDER):
        self.setFontSize(35)
        text = self.font.render(self.text,True,color,background)
        textRect = text.get_rect(center=(self.rect.centerx,self.rect.centery))
        screen.blit(text,textRect)
        pygame.display.flip()


    def buttonPressed (self):
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos[0],pos[1]):
            return True
        else:
            return False


    @property 
    def getRect(self) -> pygame.Rect:
        return self.rect
