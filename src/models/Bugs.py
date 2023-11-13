from random import randint
import pygame
from Config import SCREENHEIGHT, SCREENWIDTH


class Bug:

    def __init__(self,image:pygame.image,x:int,y:int,width:int,height:int,screen:pygame.display) -> None:
        self.x = x
        self.y = y
        self.speed = 15
        self.__pos = (x,y)
        self.width = width
        self.height = height
        self.image = image
        self.image = pygame.transform.scale(self.image,( width, height))
        self.rect = self.image.get_rect()
        self.rect.center = (self.pos)
        # self.rect.center = (randint(0,SCREENWIDTH-75),randint(0,SCREENHEIGHT-75))
        self.mask = pygame.mask.from_surface(self.image)
        self.screen = screen
        self.isBlited = False

    def blitBug(self):
        self.screen.blit(self.image,self.rect)
    
    def delBug(self):
        del Bug

    def setRandomPos(self):
        newpos = (randint(0,SCREENWIDTH-self.width),randint(0,SCREENHEIGHT-self.height))
        self.setpos(newpos)

    def moveRandom(self,speed=1.5):
        valueDir = randint(1,4)
        self.moveBug(valueDir,speed)

    def moveBug(self,valueDir,speed=1.5):
        if valueDir == 1:
            if self.rect.top > 0:
                self.rect.move_ip(0,-speed)
        if valueDir == 2:
            if self.rect.bottom < SCREENHEIGHT:
                self.rect.move_ip(0,speed)
        if valueDir == 3:
            if self.rect.left > 0:
                self.rect.move_ip(-speed,0)
        if valueDir == 4:
            if self.rect.right < SCREENWIDTH:
                self.rect.move_ip(speed,0)

    @property 
    def pos(self):
        return self.__pos
    
    @pos.setter
    def setPos(self,value:tuple):
        self.rect.center = (value)
    
    @pos.deleter
    def pos(self):
        del self.__pos

    