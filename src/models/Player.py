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
        self.rect.center = (self.x,self.y)
        self.mask = pygame.mask.from_surface(self.image)
        self.screen = screen
        self.speedY = 0
        self.speedX = 0
        

    def movePlayer(self,speed=1.5):
        key = pygame.key.get_pressed()
        if key[pygame.K_w]:
            if self.rect.top > 0:
                self.rect.move_ip(0,-speed)

        if key[pygame.K_s]:
            if self.rect.bottom < SCREENHEIGHT:
                self.rect.move_ip(0,speed)
        if key[pygame.K_a]:
            if self.rect.left > 0:
                self.rect.move_ip(-speed,0)
        if key[pygame.K_d]:
            if self.rect.right < SCREENWIDTH:
                self.rect.move_ip(speed,0)

    # def movePlayerGravity(self,speed):
    #     key = pygame.key.get_pressed()
    #     if key[pygame.K_w]:
    #         if self.rect.top > 0:
    #             self.speedY = 3
    #             self.rect.move_ip(0,-self.speedY)


    #     if key[pygame.K_a]:
    #         if self.rect.left > 0:
    #             self.rect.move_ip(-speed,0)

    #     if key[pygame.K_d]:
    #         if self.rect.right < SCREENWIDTH:
    #             self.rect.move_ip(speed,0)
        
    #     if key[pygame.K_w] == False:
    #         for i in range(6,0,-1):
    #             self.speedY = -0.5
    #         self.speedY = 0

    def blitPlayer(self):
        self.screen.blit(self.image,self.rect)
    