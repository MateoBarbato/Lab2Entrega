import pygame
from Config import SCREENHEIGHT, SCREENWIDTH
from colors import INDIGOSOFT


class Player:

    def __init__(self,image:pygame.image,x:int,y:int,width:int,height:int,screen:pygame.display) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = image
        self.image = pygame.transform.scale(self.image,( width, height))
        self.rect = self.image.get_rect()
        self.rect.center = (SCREENWIDTH/2,SCREENHEIGHT/2)
        self.mask = pygame.mask.from_surface(self.image)
        self.screen = screen
        

    def movePlayer(self,speed=1.5):
        key = pygame.key.get_pressed()
        if key[pygame.K_w]:
            self.rect.move_ip(0,-speed)
        if key[pygame.K_s]:
            self.rect.move_ip(0,speed)
        if key[pygame.K_a]:
            self.rect.move_ip(-speed,0)
        if key[pygame.K_d]:
            self.rect.move_ip(speed,0)

    def blitPlayer(self):
        self.screen.blit(self.image,self.rect)
    